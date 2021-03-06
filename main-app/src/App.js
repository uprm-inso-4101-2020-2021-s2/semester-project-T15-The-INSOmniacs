import './App.css'
import Nav from './components/Nav';
import Calendar from './components/Calendar';
import About from './components/About';
import Tasks from './components/TasksTab';
import Courses from './components/CoursesTab';
import Resources from './components/ResourcesTab';
import SignUpAndLogin from './components/SignUpAndLogin';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
    <div className="App">
      <Nav />
      <Switch>
        <Route path="/" exact component={Home}/>
        <Route path="/about" component={About}/>
        <Route path="/calendar" component={Calendar}/>
        <Route path="/tasks" component={Tasks}/>
        <Route path="/courses" component={Courses}/>
        <Route path="/resources" component={Resources}/>
        <Route path="/signupandlogin" component={SignUpAndLogin}/>
      </Switch>
    </div>
    </Router>
  );
}

const Home = () => (
  <div>
    <img src={'OfCourseLogo.jpeg'} className="ofc-logo"
        alt="logo" />
        <p>Your primary coursework organizer!</p>
  </div>
)
export default App;
