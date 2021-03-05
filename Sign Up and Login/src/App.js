import { useState, useEffect } from 'react'
import Header from './components/Header'
import SignUp from './components/SignUp'
import Button from './components/Button'
import Login from './components/Login';

function App() {

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
    const res = await fetch('http://localhost:5000/users')
    const data = await res.json()

    return data
  }

  //Add User
  const addUser = async (user) => {
    const res = await fetch('http://localhost:5000/users', {
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

export default App;
