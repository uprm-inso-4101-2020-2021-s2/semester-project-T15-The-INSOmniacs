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


    def build_map_attr(self,co_id, s_id,co_name,co_number,co_timeframe,co_professor,co_date_created,private_bool):
        result = {
            "co_id": co_id,
            "s_id": s_id,
            "co_name": co_name,
            "co_number": co_number,
            "co_timeframe": co_timeframe,
            "co_professor": co_professor,
            "co_date_created":co_date_created,
            "private":private_bool
        }
        return result

    def getAllCourses(self):
        dao = CoursesDAO()
        courses_list = dao.getAllCourses()
        result_list = [self.build_map_dict(course) for course in courses_list]
        return jsonify(result_list), 200

    def postNewCourse(self,course_json):
        s_id = course_json["s_id"]
        co_name = course_json["co_name"]
        co_number = course_json["co_number"]
        co_timeframe = course_json["co_timeframe"]
        co_professor = course_json["co_professor"]
        co_date_created = course_json["co_date_created"]
        private_bool = course_json["private"]
        dao = CoursesDAO()
        co_id = dao.post_new_course(s_id,co_name,co_number,co_timeframe,co_professor,co_date_created,private_bool)

        if co_id is None:
            return jsonify("Error in posting the course"),405 # must change for later implementation of post_new_course function


        print("POST - Course posted")
        return jsonify(self.build_map_attr(co_id, s_id,co_name,co_number,co_timeframe,co_professor,co_date_created,private_bool)),201


    def get_course_by_id(self,co_id):
        dao = CoursesDAO()
        course = dao.get_course_by_id(co_id)
        if not course:
            return jsonify("Not Found"), 404
        result_list = self.build_map_dict(course)
        return jsonify(result_list), 200

    def modify_course_by_id(self,course_json,co_id):
        s_id = course_json["s_id"]
        co_name = course_json["co_name"]
        co_number = course_json["co_number"]
        co_timeframe = course_json["co_timeframe"]
        co_professor = course_json["co_professor"]
        co_date_created = course_json["co_date_created"]
        private_bool = course_json["private"]
        dao = CoursesDAO()
        dao.modify_course_by_id(co_id,s_id,co_name,co_number,co_timeframe,co_professor,co_date_created,private_bool)

        print("MODIFIED - Course")
        return jsonify(self.build_map_attr(co_id, s_id, co_name, co_number, co_timeframe, co_professor, co_date_created,
                                           private_bool)), 201


    def delete_course_by_id(self,co_id):
        dao = CoursesDAO()
        check_if_deleted = dao.delete_course_by_id(co_id)
        if check_if_deleted:
            return jsonify("Deleted course"),200
        else:
            return jsonify("Not found"),404
