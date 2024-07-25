import './App.css';
import React from 'react';
import Conjugate from './Conjugate.js';
import AboutUs from './AboutUs.js';
import Navbar from './Navbar.js';
import MenorahPage from './MenorahPage.js';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";




function App(){
 

  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/conjugator">
          <Conjugate />
          </Route>
        <Route path="/menorah">
          <MenorahPage />
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
