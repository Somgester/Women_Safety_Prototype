import React from 'react';
import { NavLink } from 'react-router-dom';
import './navbar.css';
import { IoMdHelpCircle } from 'react-icons/io';
import { FaUserCircle } from 'react-icons/fa';

const Navbar = () => {
  return (
    <div className='nav'>
      <div className="nav-left">
        <NavLink 
          to="/" 
          exact
          style={({ isActive }) => ({
            backgroundColor: isActive ? 'black' : '',
            color: isActive ? 'white' : '',
            padding:isActive ? '15px 15px' : ''
          })}
        >
          Dashboard
        </NavLink>
        <NavLink 
          to="/analytics" 
          style={({ isActive }) => ({
            backgroundColor: isActive ? 'black' : '',
            color: isActive ? 'white' : '',
            padding:isActive ? '15px 15px' : ''
          })}
        >
          Analytics
        </NavLink>
        <NavLink 
          to="/notifications" 
          style={({ isActive }) => ({
            backgroundColor: isActive ? 'black' : '',
            color: isActive ? 'white' : '',
            padding:isActive ? '15px 15px' : ''
          })}
        >
          Notifications
        </NavLink>
      </div>
      <div className="nav-right">
        <FaUserCircle color="black" fontSize="35px" marginRight="100px"/>
        <IoMdHelpCircle color="black" fontSize="30px" />
      </div>
    </div>
  );
}

export default Navbar;
