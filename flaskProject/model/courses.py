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
        query = "select * from courses where co_id = %s"
        cursor.execute(query, (co_id,))
        course = cursor.fetchone()
        return course
    def modify_course_by_id(self,co_id,s_id,co_name,co_number,co_timeframe,co_professor,co_date_created,private_bool):
        cursor = self.conn.cursor()
        query = "update courses set s_id = (%s), co_name = (%s), co_number = (%s), co_timeframe = (%s), co_professor = (%s) \
                  ,co_date_created = (%s), private = (%s) where co_id = (%s)  "
        cursor.execute(query,(s_id, co_name, co_number, co_timeframe, co_professor, co_date_created, private_bool,co_id))
        self.conn.commit()

    def delete_course_by_id(self, co_id):
        cursor = self.conn.cursor()
        query = "delete from enrolled where co_id = (%s)"
        cursor.execute(query,(co_id,))
        query = "delete from course_tasks where co_id = (%s)"
        cursor.execute(query,(co_id,))
        query = "delete from course_resources where co_id = (%s)"
        cursor.execute(query, (co_id,))
        query = "delete from course_chats where co_id = (%s)"
        cursor.execute(query, (co_id,))
        query = "delete from courses where co_id = (%s)"
        cursor.execute(query,(co_id,))

        # Check if there was a row deleted
        affected = cursor.rowcount
        self.conn.commit()
        return affected