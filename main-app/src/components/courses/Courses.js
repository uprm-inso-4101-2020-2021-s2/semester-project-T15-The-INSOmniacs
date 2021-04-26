import Course from './Courses'

const Courses = ({ courses, onDelete, onToggle }) => {
  return (
    <>
      {courses.map((course, index) => (
        <Course key={index} course={course} onDelete={onDelete} onToggle={onToggle} />
      ))}
    </>
  )
}

export default Courses