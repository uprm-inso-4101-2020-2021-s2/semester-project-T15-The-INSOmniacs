from flask import jsonify
from model.tasks import TasksDAO


class Tasks:

    def build_attr_dict(self, t_id, t_type, t_title, t_description, t_due_date, t_due_time):
        result = {
            "t_id": t_id,
            "t_type": t_type,
            "t_title": t_title,
            "t_description": t_description,
            "t_due_date": t_due_date,
            "t_due_time": t_due_time
        }
        return result

    def build_map_dict(self, row):
        result = {
            "t_id": row[0],
            "t_type": row[1],
            "t_title": row[2],
            "t_description": row[3],
            "t_due_date": row[4],
            "t_due_time": row[5]
        }
        return result

    def getAllTasks(self):
        dao = TasksDAO()
        task_list = dao.getAllTasks()
        result_list = [self.build_map_dict(task) for task in task_list]
        return jsonify(result_list), 200

    def getTaskByID(self, t_id):
        dao = TasksDAO()
        task = dao.getTaskByID(t_id)
        if not task:
            return jsonify("Not Found"), 404
        else:
            result = self.build_map_dict(task)
            return jsonify(result), 200

    def updateTaskByID(self, old_t_id, json):
        t_id = json["t_id"]
        t_type = json["t_type"]
        t_title = json["t_title"]
        t_description = json["t_description"]
        t_due_date = json["t_due_date"]
        t_due_time = json["t_due_time"]
        dao = TasksDAO()
        edited = dao.updateTaskByID(
            t_id, t_type, t_title, t_description, t_due_date, t_due_time, old_t_id)
        if edited == 1:
            result = self.build_attr_dict(
                t_id, t_type, t_title, t_description, t_due_date, t_due_time)
            return jsonify(result), 200
        elif edited == 2:
            return jsonify("Other user has that ID"), 405
        else:
            return jsonify("Not Found"), 404

    def deleteTaskByID(self, t_id):
        dao = TasksDAO()
        executed = dao.deleteTaskByID(t_id)
        if executed:
            return jsonify("Deleted"), 200
        else:
            return jsonify("Not Found"), 404

    def getStudentTasksByID(self, s_id):
        dao = TasksDAO()
        task_list = dao.getStudentTasksByID(s_id)
        if task_list == -1:
            return jsonify("Student not found"), 404
        elif not task_list:
            return jsonify("No tasks found"), 404
        else:
            result_list = [self.build_map_dict(task) for task in task_list]
            return jsonify(result_list), 200
