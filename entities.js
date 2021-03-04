// Entities
class Student{
    constructor(Student_ID, FirstName, LastName, UniversityName, Student_email, Password, Courses){
        this.Student_ID = Student_ID;
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.UniversityName = UniversityName;
        this.Student_email = Student_email;
        this.Password = Password;
        this.Courses = Courses;
    }
}

class Course{
    constructor(Course_ID, CourseName, CourseNumber, Section, Homeworks, Exams, Projects,
        Professor, StudentsEnrolled, Chat_Link, Private, Admins, DateCreated, Resources){
            this.Course_ID = Course_ID;
            this.CourseName = CourseName;
            this.CourseNumber = CourseNumber;
            this.Section = Section;
            this.Homeworks = Homeworks;
            this.Exams = Exams;
            this.Projects = Projects;
            this.Professor = Professor;
            this.StudentsEnrolled = StudentsEnrolled;
            this.Chat_Link = Chat_Link;
            this.Private = Private;
            this.Admins = Admins;
            this.DateCreated = DateCreated;
            this.Resources = Resources;
    }
}

class Task {
    constructor(Task_ID, Task_type, Title, Description, DueDate, DaysRemaining, 
        GradePercentage, Course_ID, Student_ID, Resources){
            this.Task_ID = Task_ID;
            this.Task_type = Task_type;
            this.Title = Title;
            this.Description = Description;
            this.DueDate = DueDate;
            this.DaysRemaining = DaysRemaining;
            this.GradePercentage = GradePercentage;
            this.Course_ID = Course_ID;
            this.Student_ID = Student_ID;
            this.Resources = Resources;
    }
}

class Resource{
    constructor(Resource_ID, Title, Resource_link){
        this.Resource_ID = Resource_ID;
        this.Title = Title;
        this.Resource_link = Resource_link;
    }
}

class Calendar{
    constructor(Calendar_ID, Student_ID, Courses, Tasks){
        this.Calendar_ID = Calendar_ID;
        this.Student_ID = Student_ID;
        this.Courses = Courses;
        this.Tasks = Tasks;
    }
}

class Reminder{
    constructor(Reminder_ID, Task_type, Due_date, Task_title, Task_ID){
        this.Reminder_ID = Reminder_ID;
        this.Task_type = Task_type;
        this.Due_date = Due_date;
        this.Task_title = Task_title;
        this.Task_ID = Task_ID;
    }
}

// Example initiation
let s = new Student(10, "Bil", "Sno", "UPR", "bill@sno.com", "B!llSN0W", []);

console.log(s);