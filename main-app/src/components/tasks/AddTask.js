import { useState } from 'react'

const AddTask = ({ onAdd }) => {
  const [t_title, setTitle] = useState('')
  const [t_due_date, setDate] = useState('')
  const [t_due_time, setTime] = useState('')
  const [t_description, setDescription] = useState('')
  const [t_type, setType] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()

    if (!t_title) {
      alert('Please add a task')
      return
    }

    if (!t_due_date) {
      alert('Please state the date of your dealine/task.')
      return
    }

    onAdd({t_description, t_due_date, t_due_time, t_title, t_type})

    setTitle('')
    setDate('')
    setTime('')
    setDescription('')
    setType('')
  }

  return (
    <form className='add-form' onSubmit={onSubmit}>

      <div className='form-control'>
        <label>Task</label>
        <input
          type='text'
          placeholder='Task Title'
          value={t_title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Type</label>
        <input
          type='text'
          placeholder='Type (ex. test, homework...)'
          value={t_type}
          onChange={(e) => setType(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Date</label>
        <input
          type='date'
          placeholder=''
          value={t_due_date}
          onChange={(e) => setDate(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Time</label>
        <input
          type='time'
          placeholder=''
          value={t_due_time}
          onChange={(e) => setTime(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Description (optional)</label>
        <input
          type='text'
          placeholder='Add an optional description'
          value={t_description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>

      <input type='submit' value='Save Task' className='btn btn-block' />
    </form>
  )
}

export default AddTask