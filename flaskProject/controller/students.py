from flask import jsonify
from model.students import StudentsDAO


class Students:

    # Helper methods that facilitate json management
    def build_map_dict(self, row):
        result = {
            "s_id": row[0],
            "s_fname": row[1],
            "s_lname": row[2],
            "s_university": row[3],
            "s_email": row[4],
            "s_password": row[5]
        }
        return result

    def build_attr_dict(self, s_id, s_fname, s_lname, s_university, s_email, s_password):
        result = {}
        result['s_id'] = s_id
        result['s_fname'] = s_fname
        result['s_lname'] = s_lname
        result['s_university'] = s_university
        result['s_email'] = s_email
        result['s_password'] = s_password
        return result

    # DAO = Data Access Object

    def getAllStudents(self):
        # Execute necessary operations
        dao = StudentsDAO()
        student_list = dao.getAllStudents()
        # Modify info in a json-friendly format
        return_list = [self.build_map_dict(student) for student in student_list]
        print("GET - Students: processed")
        return jsonify(return_list)

    def addStudent(self, s_json):
        # Break down student info from the given json
        s_fname = s_json["s_fname"]
        s_lname = s_json["s_lname"]
        s_university = s_json["s_university"]
        s_email = s_json["s_email"]
        s_password = s_json["s_password"]
        dao = StudentsDAO()

        # Run the command to add a student that returns their ID
        s_id = dao.addStudent(s_fname, s_lname, s_university, s_email, s_password)

        # Return the students info with their newly generated ID as a json
        print("POST - Student: processed")
        return jsonify(self.build_attr_dict(s_id, s_fname, s_lname, s_university, s_email, s_password)), 201

    def getStudentByID(self, s_id):
        # Execute necessary operations to find the student by their ID
        dao = StudentsDAO()
        student_info = dao.getStudentByID(s_id)
        print("GET - Student: processed")
        if not student_info:
            return jsonify("Not Found"), 404
        else:
            # Return the student's info as a json
            mapped_info = self.build_map_dict(student_info)
            return jsonify(mapped_info), 200

    def updateStudentByID(self, old_s_id, s_json):
        # Break down json
        s_id = s_json["s_id"]
        s_fname = s_json["s_fname"]
        s_lname = s_json["s_lname"]
        s_university = s_json["s_university"]
        s_email = s_json["s_email"]
        s_password = s_json["s_password"]
        # Execute via DAO
        dao = StudentsDAO()
        edited = dao.updateStudentByID(s_id, s_fname, s_lname, s_university, s_email, s_password, old_s_id)
        # Return a json with the students new info
        print("PUT - Student: processed")
        if edited == 1:
            result = self.build_attr_dict(s_id, s_fname, s_lname, s_university, s_email, s_password)
            return jsonify(result), 200
        elif edited == 2:
            return jsonify("Other user has that ID"), 405
        else:
            return jsonify("Not found"), 404

    def deleteStudentByID(self, s_id):
        # Execute Order 66 on the student
        dao = StudentsDAO()
        executed = dao.deleteStudent(s_id)
        print("DELETE - Student: processed")
        if executed:
            return jsonify("DELETED"), 200
        else:
            return jsonify("NOT FOUND"), 404
