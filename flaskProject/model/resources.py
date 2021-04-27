from config.config import connect


class ResourcesDAO:
    def __init__(self):
        connect(self)

    def getAllResources(self):
        # Create a cursor that acts as our database management helper
        cursor = self.conn.cursor()
        # PostgreSQL query to be executed
        query = "select * from resources"
        cursor.execute(query)
        # Save the results our cursor received as a list of tuples
        result = [resource for resource in cursor]
        return result

    def getPersonalResourcesById(self, s_id):
        # Create a cursor that acts as our database management helper
        cursor = self.conn.cursor()

        query_test = "select * from students where s_id = %s"
        cursor.execute(query_test, (s_id,))
        if not cursor.fetchone():
            # USER NOT REGISTERED
            return None

        # PostgreSQL query to be executed
        query = "\
        select r_id, r_title, r_link, r_owner_id \
        from resources natural inner join personal_resources \
        where s_id = %s"
        cursor.execute(query, (s_id, ))
        # Save the results our cursor received as a list of tuples
        result = [resource for resource in cursor]

        return result

    def getCourseResourcesById(self, co_id):
        # Create a cursor that acts as our database management helper
        cursor = self.conn.cursor()

        query_test = "select * from courses where co_id = %s"
        cursor.execute(query_test, (co_id,))
        if not cursor.fetchone():
            # COURSE NOT REGISTERED
            return None

        # PostgreSQL query to be executed
        query = "\
        select r_id, r_title, r_link, r_owner_id \
        from resources natural inner join course_resources \
        where co_id = %s"
        cursor.execute(query, (co_id,))
        # Save the results our cursor received as a list of tuples
        result = [resource for resource in cursor]
        return result

    def getStudentResourcesById(self, s_id):
        # Create a cursor that acts as our database management helper
        cursor = self.conn.cursor()

        query_test = "select * from students where s_id = %s"
        cursor.execute(query_test, (s_id,))
        if not cursor.fetchone():
            # USER NOT REGISTERED
            return None

        # Resources
        query = " \
        select r_id, r_title, r_link, r_owner_id \
        from resources \
        where r_id IN ( \
            select r_id \
            from resources natural inner join personal_resources \
            where s_id = %s \
        ) or r_id IN ( \
            select r_id \
            from resources natural inner join enrolled natural inner join course_resources \
            where s_id = %s \
        );"

        cursor.execute(query, (s_id, s_id, ))
        # Save current results our cursor received as a list of tuples
        result = [resource for resource in cursor]

        return result

    def addResource(self, cursor, r_title, r_link, r_owner_id):

        # Make our PostgreSQL query using prepared statements (prevents SQL insertion attacks)
        query = "\
        insert into resources (r_title, r_link, r_owner_id) \
        values(%s, %s, %s) returning r_id;"
        # Execute query with the given parameters
        cursor.execute(query, (r_title, r_link, r_owner_id, ))
        # Our query should return the resources' id
        r_id = cursor.fetchone()[0]
        return r_id

    def addPersonalResource(self, r_title, r_link, r_owner_id):
        # Create our cursor
        cursor = self.conn.cursor()

        query_test = "select * from students where s_id = %s"
        cursor.execute(query_test, (r_owner_id, ))
        if not cursor.fetchone():
            # USER NOT REGISTERED
            return None

        # Use add resource helper method
        r_id = self.addResource(cursor, r_title, r_link, r_owner_id)
        # Classify the new resource as a Personal Resource
        query = "insert into personal_resources (s_id, r_id) values(%s, %s);"
        # Execute query with the given parameters
        cursor.execute(query, (r_owner_id, r_id, ))

        self.conn.commit()
        return r_id

    def addCourseResource(self, r_title, r_link, r_owner_id, co_id):
        # Create our cursor
        cursor = self.conn.cursor()

        query_test = "select * from enrolled where s_id = %s and co_id = %s"
        cursor.execute(query_test, (r_owner_id, co_id))
        if not cursor.fetchone():
            # NOT ENROLLED or USER/COURSE NOT REGISTERED
            return None

        # Use add resource helper method
        r_id = self.addResource(cursor, r_title, r_link, r_owner_id)
        # Classify the new resource as a Course Resource
        query = "insert into course_resources (co_id, r_id) values(%s, %s);"
        # Execute query with the given parameters
        cursor.execute(query, (co_id, r_id,))

        self.conn.commit()
        return r_id

    def getResourceByID(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from resources where r_id = %s"
        cursor.execute(query, (r_id, ))
        # Should return the information for the given student if they existed in the records
        r_info = cursor.fetchone()
        return r_info

    def updateResourceByID(self, r_id, r_title, r_link, r_owner_id, old_r_id):
        cursor = self.conn.cursor()
        test_query = "select r_id from resources where r_id = %s"
        cursor.execute(test_query, (old_r_id,))
        # Check if the user we want to updae exists
        if not cursor.rowcount:
            return 0

        test_query = "select r_id from resources where r_id = %s"
        cursor.execute(test_query, (r_id, ))
        # If there's another with an ID identical to the one we want to update with, we cannot update
        if cursor.rowcount and r_id != old_r_id:
            return 2

        query = "\
        update resources \
        set r_id = %s, r_title=%s, r_link=%s, r_owner_id=%s \
        where r_id=%s"
        cursor.execute(query, (r_id, r_title, r_link, r_owner_id, old_r_id, ))
        edited = cursor.rowcount
        self.conn.commit()
        return edited

    def deleteResource(self, r_id):
        cursor = self.conn.cursor()
        # Clear out relations
        query = "delete from personal_resources where r_id = %s;"
        cursor.execute(query, (r_id,))
        query = "delete from course_resources where r_id = %s;"
        cursor.execute(query, (r_id,))
        # Delete resource itself
        query = "delete from resources where r_id = %s;"
        cursor.execute(query, (r_id, ))
        # Check if there was a row deleted
        affected = cursor.rowcount
        self.conn.commit()
        return affected
