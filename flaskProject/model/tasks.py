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
