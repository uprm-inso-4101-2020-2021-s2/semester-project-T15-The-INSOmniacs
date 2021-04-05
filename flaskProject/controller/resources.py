from flask import jsonify
from model.resources import ResourcesDAO


class Resources:

    # Helper methods that facilitate json management
    def build_map_dict(self, row):
        result = {
            "r_id": row[0],
            "r_title": row[1],
            "r_link": row[2],
            "r_owner_id": row[3]
        }
        return result

    def build_attr_dict(self, r_id, r_title, r_link, r_owner_id):
        result = {
            'r_id': r_id,
            'r_title': r_title,
            'r_link': r_link,
            'r_owner_id': r_owner_id
        }
        return result

    # DAO = Data Access Object

    def getAllResources(self):
        # Execute necessary operations
        dao = ResourcesDAO()
        resource_list = dao.getAllResources()
        # Modify info in a json-friendly format
        return_list = [self.build_map_dict(resource) for resource in resource_list]
        print("GET - Resources: processed")
        return jsonify(return_list)

    def addResource(self, r_json):
        # Break down student info from the given json
        r_title = r_json["r_title"]
        r_link = r_json["r_link"]
        r_owner_id = r_json["r_owner_id"]
        dao = ResourcesDAO()

        # Run the command to add a student that returns their ID
        r_id = dao.addResource(r_title, r_link, r_owner_id)

        # Return the resources' info with its newly generated ID as a json
        print("POST - Resource: processed")
        return jsonify(self.build_attr_dict(r_id, r_title, r_link, r_owner_id)), 201

    def getResourceByID(self, r_id):
        # Execute necessary operations to find the student by their ID
        dao = ResourcesDAO()
        resource_info = dao.getResourceByID(r_id)
        print("GET - Resource: processed")
        if not resource_info:
            return jsonify("Not Found"), 404
        else:
            # Return the resources' info as a json
            mapped_info = self.build_map_dict(resource_info)
            return jsonify(mapped_info), 200

    def updateResourceByID(self, old_r_id, r_json):
        # Break down json
        r_id = r_json["r_id"]
        r_title = r_json["r_title"]
        r_link = r_json["r_link"]
        r_owner_id = r_json["r_owner_id"]
        # Execute via DAO
        dao = ResourcesDAO()
        edited = dao.updateStudentByID(r_id, r_title, r_link, r_owner_id, old_r_id)
        # Return a json with the resources' new info
        print("PUT - Resource: processed")
        if edited == 2:
            return jsonify("Other resource has that ID"), 405
        elif edited == 1:
            result = self.build_attr_dict(r_id, r_title, r_link, r_owner_id)
            return jsonify(result), 200
        else:
            return jsonify("Not found"), 404


    def deleteResourceByID(self, r_id):
        # Execute query on the resource
        dao = ResourcesDAO()
        executed = dao.deleteResource(r_id)
        print("DELETE - Resource: processed")
        if executed:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
