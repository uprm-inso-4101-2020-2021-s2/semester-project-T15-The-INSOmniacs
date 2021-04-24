from config.config import connect


class StudentsDAO:
    def __init__(self):
        connect(self)

    def loginStudent(self, s_email, s_password):
        cursor = self.conn.cursor()
        # Get the student info if the email and password match
        query = " \
        select * \
        from students \
        where s_email = %s and s_password = %s"
        # Execute query
        cursor.execute(query, (s_email, s_password, ))
        # None if credentials didn't match a student
        if not cursor.rowcount:
            return None
        # Return the info otherwise
        s_info = cursor.fetchone()
        return s_info


    def getAllStudents(self):
        # Create a cursor that acts as our database management helper
        cursor = self.conn.cursor()
        # PostgreSQL query to be executed
        query = "select * from students"
        cursor.execute(query)
        # Save the results our cursor received as a list of tuples
        result = [student for student in cursor]
        return result

    def addStudent(self, s_fname, s_lname, s_university, s_email, s_password):
        # Create our cursor
        cursor = self.conn.cursor()
        # Make our PostgreSQL query using prepared statements (prevents SQL insertion attacks)
        query = "\
        insert into students (s_fname, s_lname, s_university, s_email, s_password) \
        values(%s, %s, %s, %s, %s) returning s_id;"
        # Execute query with the given parameters
        cursor.execute(query, (s_fname, s_lname, s_university, s_email, s_password, ))
        # Our query should receive the students id
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

    def getStudentByID(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from students where s_id = %s"
        cursor.execute(query, (s_id, ))
        # Should return the information for the given student if they existed in the records
        s_info = cursor.fetchone()
        return s_info

    def updateStudentByID(self, s_id, s_fname, s_lname, s_university, s_email, s_password, old_s_id):
        cursor = self.conn.cursor()
        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (old_s_id,))
        # Check to see if the student you want to update exists
        if not cursor.rowcount:
            return 0

        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (s_id, ))
        # If there's another with an ID identical to the one we want to update with, we cannot update
        if cursor.rowcount and s_id != old_s_id:
            return 2

        query = "\
        update students \
        set s_id = %s, s_fname=%s, s_lname=%s, s_university=%s, s_email=%s, s_password=%s \
        where s_id=%s"
        cursor.execute(query, (s_id, s_fname, s_lname, s_university, s_email, s_password, old_s_id, ))
        edited = cursor.rowcount
        self.conn.commit()
        return edited

    def deleteStudent(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from students where s_id = %s;"
        cursor.execute(query, (s_id, ))
        # Check if there was a row deleted
        affected = cursor.rowcount
        self.conn.commit()
        return affected
