import '../App.css'

import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Header from './resources/Header'
import Button from './resources/Button'
import Resources from './resources/Resources'
import AddResource from './resources/AddResource'




const ResourcesTab = () => {
  const [showAddResource, setShowAddResource] = useState(false)
  const [resources, setResources] = useState([])

  useEffect(() => {
    const getResources = async () => {
      const resourcesFromServer = await fetchResources()
      setResources(resourcesFromServer)
    }

    getResources()
  }, [])

  // Fetch Resources
  const fetchResources = async () => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/resources', {method: 'GET'})
    const data = await res.json()

    return data
  }

  // Fetch Resource
  const fetchResource = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/resources/${id}`, {method: 'GET'})
    const data = await res.json()

    return data
  }

  // Add Resource
  const addResource = async (resource) => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/resources', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(resource),
    })

    const data = await res.json()

    setResources([...resources, data])

  }

  // Delete Resource
  const deleteResource = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/resources/${id}`, {
      method: 'DELETE',
    })
    res.status === 200
      ? setResources(resources.filter((resource) => resource.id !== id))
      : alert('Error Deleting This Resource')
  }

  // Toggle Reminder
  const toggleReminder = async (id) => {
    const resourceToToggle = await fetchResource(id)
    const updResource = { ...resourceToToggle, reminder: !resourceToToggle.reminder }

    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/resources/${id}`, {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(updResource),
    })

    const data = await res.json()

    setResources(
      resources.map((resource) =>
        resource.id === id ? { ...resource, reminder: data.reminder } : resource
      )
    )
  }

  //&&for no 'else'
  return (
    <div className='container'>
      <Header onAdd={() => setShowAddResource(!showAddResource)} showAdd={showAddResource}
      />
      {showAddResource && <AddResource onAdd={addResource} />}
      {resources.length > 0 ? (
      <Resources
        resources={resources}
        onDelete={deleteResource}
        onToggle={toggleReminder}
      />
      ) : (
        'There are no uploaded resources.'
      )}
    </div>
  );
}

export default ResourcesTab