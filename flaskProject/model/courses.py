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