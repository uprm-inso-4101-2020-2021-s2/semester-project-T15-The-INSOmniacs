from config.config import connect


class TasksDAO:

    def __init__(self):
        connect(self)

    def getAllTasks(self):
        cursor = self.conn.cursor()
        query = "select t_id, t_type, t_title, t_description, t_due_date, t_due_time from tasks;"
        cursor.execute(query)
        result = [task for task in cursor]
        return result

    def getTaskByID(self, t_id):
        cursor = self.conn.cursor()
        query = "select t_id, t_type, t_title, t_description, t_due_date, t_due_time from tasks where t_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def updateTaskByID(self, t_id, t_type, t_title, t_description, t_due_date, t_due_time, old_t_id):
        cursor = self.conn.cursor()
        test_query = "select t_id from tasks where t_id = %s;"
        cursor.execute(test_query, (old_t_id,))
        if(not cursor.rowcount):
            return 0

        test_query = "select t_id from tasks where t_id = %s;"
        cursor.execute(test_query, (t_id,))
        if(cursor.rowcount and t_id != old_t_id):
            return 2

        query = "\
        update tasks \
        set t_id = %s, t_type=%s, t_title=%s, t_description=%s, t_due_date=%s, t_due_time=%s \
        where t_id=%s"
        cursor.execute(query, (t_id, t_type, t_title,
                       t_description, t_due_date, t_due_time, old_t_id))
        edited = cursor.rowcount
        self.conn.commit()
        return edited

    def deleteTaskByID(self, t_id):
        cursor = self.conn.cursor()
        query = "delete from tasks where t_id = %s;"
        cursor.execute(query, (t_id,))
        executed = cursor.rowcount
        self.conn.commit()
        return executed

    def getAllPersonalTasksByID(self, s_id):
        cursor = self.conn.cursor()
        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (s_id,))
        # Check to see if the student is registered
        if not cursor.rowcount:
            return -1

        # Getting personal tasks
        query = "select t_id, t_type, t_title, t_description, t_due_date, t_due_time \
        from tasks natural inner join personal_tasks \
        where s_id = %s;"
        cursor.execute(query, (s_id,))
        result_list = [task for task in cursor]
        return result_list

    def addPersonalTask(self, t_type, t_title, t_description, t_due_date, t_due_time, s_id):
        cursor = self.conn.cursor()
        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (s_id,))
        # Check to see if the student is registered
        if not cursor.rowcount:
            return None

        # Inserting into task table
        query = "insert into tasks (t_type, t_title, t_description, t_due_date, t_due_time) \
            values (%s, %s, %s, %s, %s) returning t_id;"
        cursor.execute(
            query, (t_type, t_title, t_description, t_due_date, t_due_time))
        t_id = cursor.fetchone()[0]

        # Also, inserting into personal tasks table to differentiate between a course task
        query = "insert into personal_tasks (s_id, t_id) values (%s, %s);"
        cursor.execute(query, (s_id, t_id))

        self.conn.commit()
        return t_id

    def getAllCourseTasksByID(self, co_id):
        cursor = self.conn.cursor()
        test_query = "select co_id from courses where co_id = %s;"
        cursor.execute(test_query, (co_id,))
        # Check to see if course exists
        if not cursor.fetchone():
            return -1

         # Getting all course tasks
        query = "select t_id, t_type, t_title, t_description, t_due_date, t_due_time \
        from tasks natural inner join course_tasks \
        where co_id = %s;"
        cursor.execute(query, (co_id,))
        result_list = [task for task in cursor]
        return result_list

    def addCourseTask(self, t_type, t_title, t_description, t_due_date, t_due_time, co_id):
        cursor = self.conn.cursor()
        test_query = "select co_id from courses where co_id = %s;"
        cursor.execute(test_query, (co_id,))
        # Check to see if course exists
        if not cursor.fetchone():
            return None

        # Inserting into task table
        query = "insert into tasks (t_type, t_title, t_description, t_due_date, t_due_time) \
            values (%s, %s, %s, %s, %s) returning t_id;"
        cursor.execute(
            query, (t_type, t_title, t_description, t_due_date, t_due_time))
        t_id = cursor.fetchone()[0]

        # Also, inserting into personal tasks table to differentiate between a course task
        query = "insert into course_tasks (co_id, t_id) values (%s, %s);"
        cursor.execute(query, (co_id, t_id))

        self.conn.commit()
        return t_id

    def getStudentTasksByID(self, s_id):
        cursor = self.conn.cursor()
        test_query = "select s_id from students where s_id = %s"
        cursor.execute(test_query, (s_id,))
        # Check to see if the student is registered
        if not cursor.rowcount:
            return -1

        # Getting personal tasks
        query = "\
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

        cursor.execute(query, (s_id, s_id, ))
        result_list = [task for task in cursor]

        return result_list
