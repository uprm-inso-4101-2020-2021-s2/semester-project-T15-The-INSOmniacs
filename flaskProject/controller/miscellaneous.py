from flask import jsonify
from model.miscellaneous import MiscellaneousDAO
from datetime import datetime


class Miscellaneous:

    # Helper methods
    def hour_to_minutes(self, time):
        # Time format: hh:mm
        hour = time[:2]
        minutes = time[3:]
        return int(hour) * 60 + int(minutes)

    # An event should have: id, type, title, date, time
    def course_to_event(self, course):
        e_id = course[0]
        e_title = course[2]
        e_type = "course"

        # Time to split strings
        e_time = course[4][:5]

        # Weekdays are determined by the section
        co_number = course[3]
        section = co_number[-3:]
        weekdays = [0, 2, 4] if int(section) % 10 <= 5 else [1, 3]
        today = datetime.today()

        e_date = today.strftime("%m/%d/%Y") if (today.weekday() in weekdays) else None

        '''
        if today.weekday() > 4:
            e_weekday = weekdays[0]

        class_minutes = self.hour_to_minutes(e_time)
        today_minutes = self.hour_to_minutes(today.time().strftime("%H:%M"))

        class_over = today.weekday() in weekdays and today_minutes > class_minutes
        e_date = weekdays[0]
        '''

        event = {
            "e_id": e_id,
            "e_type": e_type,
            "e_title": e_title,
            "e_date": e_date,
            "e_time": e_time
        }
        return event

    # An event should have: id, type, title, date, time
    def task_to_event(self, task):
        # Task schema: t_id, t_type, t_title, t_description, t_date, t_time
        event = {
            "e_id": task[0],
            "e_type": task[1],
            "e_title": task[2],
            "e_date": task[4],
            "e_time": task[5]
        }

        return event

    def getUpcomingEvents(self, s_id):
        dao = MiscellaneousDAO()

        tasks, courses = dao.getUpcomingEvents(s_id)

        if not tasks and not courses:
            return jsonify("Not Found"), 404

        events = []

        for task in tasks:
            t_event = self.task_to_event(task)
            events.append(t_event)
        for course in courses:
            c_event = self.course_to_event(course)
            if c_event["e_date"]:
                events.append(c_event)

        curr_day = datetime.today().strftime("%m/%d/%Y")
        weekday = datetime.today().weekday()  # {Mo, Tu, We, Th, Fr, Sa, Su} -> {0, 1, ..., 6}
        curr_time = datetime.now().strftime("%H:%M")
        curr_minutes = self.hour_to_minutes(curr_time)
        curr_datetime = datetime.today()

        upcoming_events = []
        for event in events:
            e_type = event["e_type"]
            e_minutes = self.hour_to_minutes(event["e_time"])
            e_date = event["e_date"]
            e_time = event["e_time"]
            e_datetime = datetime(int(e_date[-4:]), int(e_date[:2]), int(e_date[3:5]),
                                  int(e_time[:2]), int(e_time[3:]), 0)
            print("E_Datetime:", e_datetime)
            print("C_Datetime:", curr_datetime)
            print("Diff", e_datetime - curr_datetime)
            print()

            time_difference = (e_datetime - curr_datetime).seconds + (e_datetime - curr_datetime).days * 86400
            if e_type == "course" and 0 < e_minutes - curr_minutes <= 60:
                event["e_time_remaining"] = (e_minutes - curr_minutes) * 60
                upcoming_events.append(event)
            elif e_type == "project" and 0 < time_difference <= 432000 \
                    or (e_type == "exam" and 0 < time_difference <= 259200) \
                    or ((e_type == "report" or e_type == "homework") and 0 < time_difference <= 172800) \
                    or (0 < time_difference <= 86400):
                event["e_time_remaining"] = time_difference
                upcoming_events.append(event)

        return jsonify(upcoming_events)

        # '''
        # Exam: 3 days = 259200 seconds
        # Project: 5 days = 432000 seconds
        # Homework: 2 days = 172800 seconds
        # Study: 1 day = 86400 seconds
        # Presentation: 1 day = 86400 seconds
        # Report: 2 days = 172800 seconds
        # Course: 1 hr
        # '''
