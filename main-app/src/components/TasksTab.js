import '../App.css'

import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Header from './tasks/Header'
import Tasks from './tasks/Tasks'
import AddTask from './tasks/AddTask'
import Button from './tasks/Button'

const TasksTab = () => {
  const [showAddTask, setShowAddTask] = useState(false)
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks()
      setTasks(tasksFromServer)
    }

    getTasks()
  }, [])

  // Fetch Tasks
  const fetchTasks = async () => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/tasks/', {method: 'GET'})
    const data = await res.json()

    return data
  }

  // Fetch Task
  const fetchTask = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/tasks/${id}`,{ method: 'GET'})
    const data = await res.json()

    return data
  }

  // Add Task
  const addTask = async (task) => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/tasks/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(task),
    })

    const data = await res.json()

    setTasks([...tasks, data])

  }

  // Delete Task
  const deleteTask = async (id) => {
    const res = await fetch(`https://of-course-app.herokuapp.com/OfCourse/tasks/${id}`, { method: 'DELETE'})
    res.status === 200
      ? setTasks(tasks.filter((task) => task.t_id !== id))
      : alert('Error Deleting This Task')
  }

  //&&for no 'else'
  return (
    <div className='container'>
      <Header onAdd={() => setShowAddTask(!showAddTask)} showAdd={showAddTask}
      />
      {showAddTask && <AddTask onAdd={addTask} />}
      {tasks.length > 0 ? (
      <Tasks
        tasks={tasks}
        onDelete={deleteTask}
      />
      ) : (
        'Congrats! You have no pending assignments or tasks.'
      )}
    </div>
  );
}

export default TasksTab