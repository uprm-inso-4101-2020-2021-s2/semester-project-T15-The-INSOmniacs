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

    def addResource(self, r_title, r_link, r_owner_id):
        # Create our cursor
        cursor = self.conn.cursor()
        # Make our PostgreSQL query using prepared statements (prevents SQL insertion attacks)
        query = "\
        insert into resources (r_title, r_link, r_owner_id) \
        values(%s, %s, %s) returning r_id;"
        # Execute query with the given parameters
        cursor.execute(query, (r_title, r_link, r_owner_id, ))
        # Our query should receive the students id
        r_id = cursor.fetchone()[0]
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
        query = "delete from resources where r_id = %s;"
        cursor.execute(query, (r_id, ))
        # Check if there was a row deleted
        affected = cursor.rowcount
        self.conn.commit()
        return affected
