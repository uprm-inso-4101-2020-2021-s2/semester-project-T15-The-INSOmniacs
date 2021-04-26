import './App.css'
import Nav from './components/Nav';
import Calendar from './components/Calendar';
import About from './components/About';
import Tasks from './components/TasksTab';
import Courses from './components/CoursesTab';
import Resources from './components/Resources';
import SignUpAndLogin from './components/SignUpAndLogin';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
    <div className="App">
      <Nav />
      <Switch>
        <Route path="/" exact component={Dashboard}/>
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

const Dashboard = () => (
  <div>
    <h1> Dashboard</h1>
  </div>
)
export default App;
