import '../App.css'

import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Header from './courses/Header'
import Button from './courses/Button'
import Courses from './courses/Courses'
import AddCourse from './courses/AddCourse'




const CoursesTab = () => {
  const [showAddCourse, setShowAddCourse] = useState(false)
  const [courses, setCourses] = useState([])

  useEffect(() => {
    const getCourses = async () => {
      const coursesFromServer = await fetchCourses()
      setCourses(coursesFromServer)
    }

    getCourses()
  }, [])

  // Fetch Courses
  const fetchCourses = async () => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/courses', {method: 'GET'})
    const data = await res.json()

    return data
  }

  // Fetch Course
  const fetchCourse = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/courses/${id}`, {method: 'GET'})
    const data = await res.json()

    return data
  }

  // Add Course
  const addCourse = async (course) => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/courses', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(course),
    })

    const data = await res.json()

    setCourses([...courses, data])

  }

  // Delete Course
  const deleteCourse = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/courses/${id}`, {
      method: 'DELETE',
    })
    res.status === 200
      ? setCourses(courses.filter((course) => course.id !== id))
      : alert('Error Deleting This Course')
  }

  // Toggle Reminder
  const toggleReminder = async (id) => {
    const courseToToggle = await fetchCourse(id)
    const updCourse = { ...courseToToggle, reminder: !courseToToggle.reminder }

    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/courses/${id}`, {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(updCourse),
    })

    const data = await res.json()

    setCourses(
      courses.map((course) =>
        course.id === id ? { ...course, reminder: data.reminder } : course
      )
    )
  }

  //&&for no 'else'
  return (
    <div className='container'>
      <Header onAdd={() => setShowAddCourse(!showAddCourse)} showAdd={showAddCourse}
      />
      {showAddCourse && <AddCourse onAdd={addCourse} />}
      {courses.length > 0 ? (
      <Courses
        courses={courses}
        onDelete={deleteCourse}
        onToggle={toggleReminder}
      />
      ) : (
        'There are no registered courses.'
      )}
    </div>
  );
}

export default CoursesTab