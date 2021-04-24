import { FaTimes } from 'react-icons/fa'

const Task = ({ task, onDelete }) => {
  return (
    <div
      className={`task`}
    >
      <h3>
        {task.t_title}
        <FaTimes
          style={{ color: 'red', cursor: 'pointer' }}
          onClick={() => onDelete(task.t_id)}
        />
      </h3>
      <h4>{task.t_due_date} </h4>
      <h4>{task.t_due_time}</h4>
      <p>{task.t_description}</p>
    </div>
  )
}

export default Task