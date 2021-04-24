import '../App.css'
import { useState, useEffect } from 'react'
import Header from './signupandlogin/Header'
import SignUp from './signupandlogin/SignUp'
import Button from './signupandlogin/Button'
import Login from './signupandlogin/Login';

function SignUpAndLogin() {

  const [showLogin, setShowLogin] = useState(true)

  const [users, setUsers] = useState([])

  useEffect(() => {
    const getUsers = async () => {
      const usersFromServer =  await fetchUsers()
      setUsers(usersFromServer)
    }
    getUsers()
  }, [])

  //Fetch Users
  const fetchUsers = async () => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/students/')
    const data = await res.json()

    return data
  }

  //Add User
  const addUser = async (user) => {
    const res = await fetch('https://of-course-app.herokuapp.com/OfCourse/students/', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(user),
    })

    const data = await res.json()
    setUsers([...users, data])

  }

  return (
    <div className="container">
      <Header title={showLogin ? 'Log in to Of Course!' : 'Of Course! SignUp'}/>
      {showLogin ? <Login /> : <SignUp onAdd={addUser}/>}
      <div className="footer">
        <Button 
          color='grey' 
          text={showLogin ? 'Sign Up (Create new account)' : 'Login'}
          onClick={() => setShowLogin(!showLogin)}
          />
      </div>
    </div>
  );
}

export default SignUpAndLogin;