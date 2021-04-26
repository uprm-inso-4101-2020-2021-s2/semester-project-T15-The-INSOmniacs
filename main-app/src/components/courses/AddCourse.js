import { useState } from 'react'

const AddCourse = ({ onAdd }) => {
  
  const [course, setCourseName] = useState('')
  const [professor, setProfessor] = useState('')
  const [code, setCode] = useState('')
  const [section, setSection] = useState('')
  const [schedule, setSchedule] = useState('')
  const [location, setLocation] = useState('')
  const [priv, setPriv] = useState(false)

  const onSubmit = (e) => {
    e.preventDefault()

    if (!course) {
      alert('Please add a name to your course')
      return
    }

    // if (!code) {
    //   alert('Please add a code your course.')
    //   return
    // }

    onAdd({ professor, course, code, schedule, location, priv })

    setProfessor('')
    setCourseName('')
    setCode('')
    setSchedule('')
    setLocation('')
    setPriv(false)
  }

  return (
    <form className='add-form' onSubmit={onSubmit}>
      <div className='form-control'>
        <label>Course Name</label>
        <input
          type='text'
          placeholder='Course Name'
          value={course}
          onChange={(e) => setCourseName(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Course Code</label>
        <input
          type='text'
          placeholder='Ex. INSO4101, 6.0001, etc.'
          value={code}
          onChange={(e) => setCode(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Section</label>
        <input
          type='text'
          placeholder='Section ID'
          value={section}
          onChange={(e) => setSection(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Professor's Name</label>
        <input
          type='text'
          placeholder='Professor Name'
          value={professor}
          onChange={(e) => setProfessor(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Course Schedule</label>
        <input
          type='text'
          placeholder='Ex. "Mon, Wed, and Fri at 10:30am"'
          value={schedule}
          onChange={(e) => setSchedule(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>Location (Room, Building, Platform, etc.)</label>
        <input
          type='text'
          placeholder='Ex. S-113, Google Meet, etc.'
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />
      </div>
      <div className='form-control form-control-check'>
        <label>Set Private</label>
        <input
          type='checkbox'
          checked={priv}
          value={priv}
          onChange={(e) => setPriv(e.currentTarget.checked)}
        />
      </div>

      <input type='submit' value='Save Course' className='btn btn-block' />
    </form>
  )
}

export default AddCourse