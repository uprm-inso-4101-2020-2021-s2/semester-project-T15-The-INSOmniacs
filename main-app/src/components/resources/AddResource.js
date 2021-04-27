import { useState } from 'react'

const AddResource = ({ onAdd }) => {
  
  const [resource, setResourceName] = useState('')
  const [file, setFile] = useState('')

  const onSubmit = (e) => {
    e.preventDefault()

    if (!resource) {
      alert('Please add a name to your resource')
      return
    }

    // if (!file) {
    //   alert('Please add a file your resource.')
    //   return
    // }

    onAdd({ resource, file })

    setResourceName('')
    setFile('')
  }

  return (
    <form className='add-form' onSubmit={onSubmit}>
      <div className='form-control'>
        <label>Resource Name</label>
        <input
          type='text'
          placeholder='Resource Name'
          value={resource}
          onChange={(e) => setResourceName(e.target.value)}
        />
      </div>
      <div className='form-control'>
        <label>File</label>
        <input
          type='text'
          placeholder='Paste a link to your Resource File'
          value={file}
          onChange={(e) => setFile(e.target.value)}
        />
      </div>
      

      <input type='submit' value='Save Resource' className='btn btn-block' />
    </form>
  )
}

export default AddResource