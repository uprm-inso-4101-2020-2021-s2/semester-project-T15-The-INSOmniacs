import PropTypes from 'prop-types'


const Header = ({title}) => {

    return (
        <header className='header'>
            <h1>{title}</h1>
        </header>
    )
}

Header.defaultProps = {
    title: 'Sign Up',
}

Header.propTypes = {
    title: PropTypes.string,
}

// const headingStyle = {
//     color: 'red', 
//     backgroundColor: 'black',
// }

export default Header