import { FaTimes } from 'react-icons/fa'

const User = ({ user , onDelete }) => {
    return (
        <div className="user">
            <h3>
                {user.s_fname} <FaTimes style={{ color: 'red', cursor: 'pointer'}}
                onClick={() => onDelete(user.s_id)}/>
            </h3>
            <p>{user.s_email}</p>
        </div>
    )
}

export default User