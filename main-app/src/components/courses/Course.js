import { FaTimes } from 'react-icons/fa'

const Course = ({ course, onDelete, onToggle }) => {
  return (
    <div
      className={`course ${course.priv ? 'priv' : ''}`}
      onDoubleClick={() => onToggle(course.id)}
    >
      <h3>
        {course.text}{' '}{course.course}
        <FaTimes
          style={{ color: 'red', cursor: 'pointer' }}
          onClick={() => onDelete(course.id)}
        />
      </h3>
      <h4>{course.day} </h4>
      <h4>{course.time}</h4>
      <p>{course.description}</p>
    </div>
  )
}

export default Course