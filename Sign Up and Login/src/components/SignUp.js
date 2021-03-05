import { useState } from 'react'
import { useForm } from 'react-hook-form'

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEye } from "@fortawesome/free-solid-svg-icons";

const SignUp = ( { onAdd } ) => {
    const [name, setName]= useState('')
    const [email, setEmail]= useState('')
    const [password, setPassword]= useState('')
    const [passwordConfirmation, setPasswordConfirmation] = useState('')

    const [hiddenPassword, setHiddenPassword] = useState(true)
    const toggleHiddenPassword = () => {
        setHiddenPassword(!hiddenPassword)
    }
    const eye = <FontAwesomeIcon icon = {faEye} />;

    const onSubmit = (e) => {
        e.preventDefault()
        if(!name) {
            alert('Please add your name')
            return
        }
        if(!email) {
            alert('Enter a valid email')
            return
        }
        if(password != passwordConfirmation) {
            alert('Passwords must match')
            return
        }
        if(password.length > 12 || password.length < 5) {
            alert("Password size must be: 5-12 characters.")
            return
        }

        onAdd({ name, email, password, passwordConfirmation })

        setName('')
        setEmail('')
        setPassword('')
        setPasswordConfirmation('')
    }
    return (
        <form className='add-form' onSubmit={onSubmit}>

            <div className='form-control'>
                <label>First and last name</label>
                <input type='text' placeholder='name' value={name} onChange={(e) => setName(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>Email</label>
                <input type='text' placeholder='email' value={email} onChange={(e) => setEmail(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>Password</label>
                <input 
                    type={hiddenPassword ? "password" : "text"} 
                    placeholder='password' 
                    name="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <i onClick={toggleHiddenPassword}> {eye} </i>{" "}
            </div>

            <div className='form-control'>
                <label>Confirm password</label>
                <input 
                    type={hiddenPassword ? "password" : "text"} 
                    placeholder='re-enter password' 
                    name="password"
                    value={passwordConfirmation}
                    onChange={(e) => setPasswordConfirmation(e.target.value)}
                />
                <i onClick={toggleHiddenPassword}> {eye} </i>{" "}
            </div>

            <input type='submit' value='Sign Up'
            className='btn btn-block'/>
            
        </form>
    )
}

export default SignUp
