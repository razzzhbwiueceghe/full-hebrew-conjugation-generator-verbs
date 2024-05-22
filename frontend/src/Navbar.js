import React, {useState} from 'react';
import './Navbar.css';
import {Link} from 'react-router-dom';

function Navbar() {
  // adding the states
  const [isActive, setIsActive] = useState(false);

  //add the active class
  const toggleActiveClass = () => {
    setIsActive(!isActive);
  };

  //clean up function to remove the active class
  const removeActive = () => {
    setIsActive(false)
  }

  return (


        <nav className={'navbar'}>

          {/* logo */}
          <h1 className={'logo'}>
          <Link to='/'>
          Shorazim
          </Link>
          </h1>

          <ul className={'navMenu '+(isActive ? 'active' : '')}>
            <li onClick={removeActive}>
              <Link to='/aboutus' className={'navLink'}>About Us</Link>
            </li>
            <li onClick={removeActive}>
              <Link to='/conjugator' className={'navLink'}>Conjugator</Link>
            </li>
            <li onClick={removeActive}>
              <Link to='/verbparser' className={'navLink'}>Verb Parser</Link>
            </li>
          </ul>

          <div className={'hamburger '+(isActive ? 'active' : '')}  onClick={toggleActiveClass}>
            <span className={'bar'}></span>
            <span className={'bar'}></span>
            <span className={'bar'}></span>
          </div>
        </nav>


  );
}

export default Navbar;
