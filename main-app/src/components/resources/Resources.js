import Resource from './Resource'

const Resources = ({ resources, onDelete, onToggle }) => {
  return (
    <>
      {resources.map((resource, index) => (
        <Resource key={index} resource={resource} onDelete={onDelete} onToggle={onToggle} />
      ))}
    </>
  )
}

export default Resources