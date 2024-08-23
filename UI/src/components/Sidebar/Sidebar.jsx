import React from 'react';
import './sidebar.css';
import { GrRestroomWomen } from 'react-icons/gr';
import { FaPhone } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
const Sidebar = () => {
  return (
    <div className='sidebar'>
      <h1><GrRestroomWomen /> Safelytics</h1>
      <div className="filter-box">
        <h3 style={{color:"gray", fontSize:"25px", fontWeight:"bold", marginBottom:"5px"}}>Search Filter</h3>
        <form >
          {/* City Name */}
          <div className="form-group">
            <label htmlFor="cityName">City Name:</label>
            <input type="text" id="cityName" name="cityName" placeholder="Enter city name" />
          </div>

          {/* Section: Case Types */}
          <div className="form-group">
            <label>Section:</label>
            <div className="checkbox-group">
              <label>
                <input type="checkbox" name="caseType" value="molestation" />
                Molestation
              </label>
              <label>
                <input type="checkbox" name="caseType" value="kidnapping" />
                Kidnapping
              </label>
              <label>
                <input type="checkbox" name="caseType" value="rape" />
                Rape Cases
              </label>
              <label>
                <input type="checkbox" name="caseType" value="murder" />
                Murder Cases
              </label>
            </div>
          </div>

          {/* Graph Type */}
          <div className="form-group">
            <label>Graphs:</label>
            <div className="checkbox-group">
              <label>
                <input type="checkbox" name="graphType" value="line" />
                Line
              </label>
              <label>
                <input type="checkbox" name="graphType" value="pie" />
                Pie
              </label>
              <label>
                <input type="checkbox" name="graphType" value="bar" />
                Bar
              </label>
            </div>
          </div>

          {/* Submit Button */}
          <button type="submit">Apply Filters</button>
        </form>
      </div>
      <div className="contact">
      <h3 style={{color:"gray", fontSize:"15px", fontWeight:"bold", marginBottom:"5px"}}>Contact Software head</h3>
        <p> <FaPhone/>8957298885</p>
        <p><MdEmail/>kuldeepagrahari9103@gmail.com</p>
      </div>
      <div className="footer">
       

        <p>&copy; Women Crime Data Analysis</p>
      </div>
    </div>
  );
}

export default Sidebar;
