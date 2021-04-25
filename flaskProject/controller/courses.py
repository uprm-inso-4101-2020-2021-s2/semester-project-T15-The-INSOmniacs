from flask import jsonify
from model.courses import CoursesDAO

class Courses:
    def build_map_dict(self, row):
        result = {
            "co_id": row[0],
            "s_id": row[1],
            "co_name": row[2],
            "co_number": row[3],
            "co_timeframe": row[4],
            "co_professor": row[5],
            "co_date_created":row[6],
            "private":row[7]
        }
        return result

    def getAllCourses(self):
        dao = CoursesDAO()
        courses_list = dao.getAllCourses()
        result_list = [self.build_map_dict(course) for course in courses_list]
        return jsonify(result_list), 200

    def postNewCourse(self,course_json):
        co_id = course_json["co_id"]
        s_id = course_json["s_id"]
        co_name = course_json["co_name"]
        co_number = course_json["co_number"]
        co_timeframe = course_json["co_professor"]
        co_professor = course_json["co_professor"]
        co_date_created = course_json["co_date_created"]
        private_bool = course_json["private"]
        dao = CoursesDAO()