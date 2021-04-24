import User from './User'

const Users = ({users, onDelete}) => {
   

    return (
        <>
        {users.map((user, index) => (
            <User 
            key={index}
            user={user} 
            onDelete={onDelete}/>
        ))}
            
        </>
    )
}

export default Users