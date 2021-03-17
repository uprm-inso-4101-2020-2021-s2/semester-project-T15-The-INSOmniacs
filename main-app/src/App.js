import './App.css'
import Nav from './components/Nav';
import Calendar from './components/Calendar';
import About from './components/About';
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
