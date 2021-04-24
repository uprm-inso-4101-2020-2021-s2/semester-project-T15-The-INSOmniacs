import '../App.css'
import {Link} from 'react-router-dom';

function Nav() {
    const navStyle = {
        color: 'white'
    };

  return (
    <nav>
        <Link style={navStyle} to="/signupandlogin">
            <li>SignUp/Login</li>
        </Link> 
        <Link style={navStyle} to="/">
                <h3>Logo</h3>
        </Link>
        <ul className="nav-links">
            <Link style={navStyle} to="/calendar">
                <li>Calendar</li>
            </Link>
            <Link style={navStyle} to="/courses">
                <li>Courses</li>
            </Link>
            <Link style={navStyle} to="/tasks">
                <li>Tasks</li>
            </Link>
            <Link style={navStyle} to="/resources">
                <li>Resources</li>
            </Link>
            <Link style={navStyle} to="/about">
                <li>About</li>
            </Link>
        </ul>
    </nav>
  );
}

export default Nav;
