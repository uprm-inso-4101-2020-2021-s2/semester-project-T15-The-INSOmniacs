from config.config import connect


# from model.courses import CoursesDAO Miscellaneous


class MiscellaneousDAO:
    def __init__(self):
        connect(self)

    def getUpcomingEvents(self, s_id):
        cursor = self.conn.cursor()

        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (s_id,))
        # Check to see if the student exists
        if not cursor.rowcount:
            return 0

        # Getting tasks
        query = " \
        select t_id, t_type, t_title, t_description, t_due_date, t_due_time \
        from tasks \
        where t_id IN ( \
            select t_id \
            from tasks natural inner join personal_tasks \
            where s_id = %s \
        ) or t_id IN ( \
            select t_id \
            from tasks natural inner join enrolled natural inner join course_tasks \
            where s_id = %s \
        );"
        cursor.execute(query, (s_id, s_id,))

        task_list = [task for task in cursor]

        # Getting enrolled courses
        query = " \
        select C.co_id, C.s_id, co_name, co_number, co_timeframe, co_professor, co_date_created, private \
        from courses as C inner join enrolled as E on C.co_id = E.co_id \
        where E.s_id = %s;"

        cursor.execute(query, (s_id, ))

        course_list = [course for course in cursor]

        return task_list, course_list
