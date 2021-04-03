from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/OfCourse/')
def home():
    return "home"

# User Management Routes

@app.route("/OfCourse/users/")
def addUser():
    return "foo"

# Course Management Routes

@app.route("/OfCourse/courses/")
def addCourse():
    return "foo"

# Task Management Routes

@app.route("/OfCourse/tasks/")
def addTask():
    return "foo"

# Resource Management Routes

@app.route("/OfCourse/resources/")
def addResource():
    return "foo"

# Calendar Management Routes

app.route("/OfCourse/calendars/")
def getCalendar():
    return "foo"


if __name__ == '__main__':
    app.run(debug=True)
