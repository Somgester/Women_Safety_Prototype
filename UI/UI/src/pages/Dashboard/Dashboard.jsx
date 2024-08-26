import React from 'react';
import { FaExclamationTriangle, FaMapMarkerAlt, FaRegFileAlt } from 'react-icons/fa';
import "./Dashboard.css";

import {Link} from "react-router-dom"


const Dashboard = () => {
    return (
        <div className='dash'>
            <div className="summary">
                <div className="sum-box count-box">
                    <FaRegFileAlt size={30} />
                    <h2>Total Cases in last 30 days</h2>
                    <p>1,230</p>

                    <Link to="/analytics"><button style={{backgroundColor:"rgb(158, 183, 244)"}}>Know More</button></Link>

                   

                </div>
                <div className="sum-box hotspot">
                    <FaMapMarkerAlt size={30} />
                    <h2>Hotspots</h2>
                    <p>5 Active Hotspots</p>

                    <Link to="/analytics"><button style={{backgroundColor:"rgb(253, 202, 137)"}}>See the analytics</button></Link>

                

                </div>
                <div className="sum-box emergency-alert">
                    <FaExclamationTriangle size={30} />
                    <h2>Emergency Alerts</h2>
                    <p>3 Alerts in Last 24 Hours</p>

                    <Link to="/notifications"><button style={{backgroundColor:"pink"}}>See all</button></Link>


                </div>
            </div>

            <div className="map">
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d117368.24373338332!2d79.96454726803869!3d23.17904492468473!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3981a9715ba1923d%3A0xba3ef8a2be6b0ccf!2sKhamaria%2C%20Jabalpur%2C%20Madhya%20Pradesh%20482005!5e0!3m2!1sen!2sin!4v1724109031529!5m2!1sen!2sin"
                    width="100%"
                    height="100%"
                    style={{ border: 0 }}
                    allowFullScreen=""
                    loading="lazy"
                    referrerPolicy="no-referrer-when-downgrade"
                    title="Google Maps Embed"
                ></iframe>
            </div>
        </div>
    )
}

export default Dashboard;
