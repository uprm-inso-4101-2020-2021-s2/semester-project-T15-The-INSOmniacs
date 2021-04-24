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

