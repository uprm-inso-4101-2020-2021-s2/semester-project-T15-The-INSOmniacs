import { FaTimes } from 'react-icons/fa'

const Resource = ({ resource, onDelete, onToggle }) => {
  return (
    <div
      className={`resource ${resource.priv ? 'priv' : ''}`}
      onDoubleClick={() => onToggle(resource.id)}
    >
      <h3>
        {resource.text}{' '}{resource.resource}
        <FaTimes
          style={{ color: 'red', cursor: 'pointer' }}
          onClick={() => onDelete(resource.id)}
        />
      </h3>
      <h4>{resource.day} </h4>
      <h4>{resource.time}</h4>
      <p>{resource.description}</p>
    </div>
  )
}

export default Resource