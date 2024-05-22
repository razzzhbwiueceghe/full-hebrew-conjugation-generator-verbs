import './App.css';
import React from 'react';
import Conjugate from './Conjugate.js';
import AboutUs from './AboutUs.js';
import Navbar from './Navbar.js';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";




function App(){
  //this where are user log in logic will go
  //network cache would also go here

  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/conjugator">
          <Conjugate />
        </Route>
        <Route path="/aboutus">
          <AboutUs />
        </Route>
        <Redirect from="/" to="/aboutus" />
      </Switch>
    </Router>
  );
}



export default App;
