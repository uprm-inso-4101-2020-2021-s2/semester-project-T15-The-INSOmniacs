import { useState } from 'react'
import { useForm } from 'react-hook-form'

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faEye } from "@fortawesome/free-solid-svg-icons";

const SignUp = ( { onAdd } ) => {
    const [s_fname, setFName]= useState('')
    const [s_lname, setLName]= useState('')
    const [s_email, setEmail]= useState('')
    const [s_university, setUniversity]= useState('')
    const [s_password, setPassword]= useState('')
    const [passwordConfirmation, setPasswordConfirmation] = useState('')

    const [hiddenPassword, setHiddenPassword] = useState(true)
    const toggleHiddenPassword = () => {
        setHiddenPassword(!hiddenPassword)
    }
    const eye = <FontAwesomeIcon icon = {faEye} />;

    const onSubmit = (e) => {
        e.preventDefault()
        if(!s_fname) {
            alert('Please add your name')
            return
        }
        if(!s_email) {
            alert('Enter a valid email')
            return
        }
        if(s_password != passwordConfirmation) {
            alert('Passwords must match')
            return
        }
        if(s_password.length > 12 || s_password.length < 5) {
            alert("Password size must be: 5-12 characters.")
            return
        }

        onAdd({ s_email, s_fname, s_lname, s_password,  s_university})

        setFName('')
        setLName('')
        setEmail('')
        setUniversity('')
        setPassword('')
        setPasswordConfirmation('')
    }
    return (
        <form className='add-form' onSubmit={onSubmit}>

            <div className='form-control'>
                <label>First Name</label>
                <input type='text' placeholder='first name' value={s_fname} onChange={(e) => setFName(e.target.value)}/>
            </div>

            
            <div className='form-control'>
                <label>Last Name</label>
                <input type='text' placeholder='last name' value={s_lname} onChange={(e) => setLName(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>Email</label>
                <input type='text' placeholder='email' value={s_email} onChange={(e) => setEmail(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>University</label>
                <input type='text' placeholder='university' value={s_university} onChange={(e) => setUniversity(e.target.value)}/>
            </div>

            <div className='form-control'>
                <label>Password</label>
                <input 
                    type={hiddenPassword ? "password" : "text"} 
                    placeholder='password' 
                    name="password"
                    value={s_password}
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
