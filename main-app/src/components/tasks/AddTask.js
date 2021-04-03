import { useState } from 'react'

const AddTask = ({ onAdd }) => {
  const [course, setCourse] = useState('')
  const [text, setText] = useState('')
  const [day, setDay] = useState('')
  const [time, setTime] = useState('')
  const [description, setDescription] = useState('')
  const [reminder, setReminder] = useState(false)

  const onSubmit = (e) => {
    e.preventDefault()

    if (!text) {
      alert('Please add a task')
      return
    }

    if (!day) {
      alert('Please state the date of your dealine/task.')
      return
    }

    onAdd({ course, text, day, time, description, reminder })

    setCourse('')
    setText('')
    setDay('')
    setTime('')
    setDescription('')
    setReminder(false)
  }

  return (
    <form className='add-form' onSubmit={onSubmit}>
      <div className='form-control'>
        <label>Select course</label>
        <input
          type='text'
          placeholder='Select Course'
          value={course}
          onChange={(e) => setCourse(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Task</label>
        <input
          type='text'
          placeholder='Task Title'
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Date</label>
        <input
          type='date'
          placeholder=''
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Time</label>
        <input
          type='time'
          placeholder=''
          value={time}
          onChange={(e) => setTime(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Description (optional)</label>
        <input
          type='text'
          placeholder='Add an optional description'
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <div className='form-control form-control-check'>
        <label>Set Reminder</label>
        <input
          type='checkbox'
          checked={reminder}
          value={reminder}
          onChange={(e) => setReminder(e.currentTarget.checked)}
        />
      </div>

      <input type='submit' value='Save Task' className='btn btn-block' />
    </form>
  )
}

export default AddTask