from config.config import connect


class CoursesDAO:

    def __init__(self):
        connect(self)



    def getAllCourses(self):
        cursor = self.conn.cursor()
        query = "select * from courses;"
        cursor.execute(query)
        result = [course for course in cursor]
        return result

    def post_new_course(self,s_id, co_name, co_number, co_timeframe, co_professor, co_date_created, private_bool):
        cursor = self.conn.cursor()
        query = "insert into courses (s_id, co_name, co_number, co_timeframe, co_professor, co_date_created, private) \
                values(%s, %s, %s , %s , %s , %s , %s) returning co_id;"
        cursor.execute(query,(s_id, co_name, co_number, co_timeframe, co_professor, co_date_created, private_bool))
        co_id = cursor.fetchone()[0]
        self.conn.commit()
        return co_id

    def get_course_by_id(self, co_id):
        cursor = self.conn.cursor()