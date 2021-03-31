import './App.css'
import Nav from './components/Nav';
import Calendar from './components/Calendar';
import About from './components/About';
import Tasks from './components/Tasks';
import Courses from './components/Courses';
import Resources from './components/Resources';
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
