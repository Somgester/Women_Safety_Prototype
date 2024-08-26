import React from 'react';
import "./card.css";
import { FaExclamationTriangle } from 'react-icons/fa';

const NotificationCard = ({ timestamp, location, message }) => {
  return (
    <div className='not-card'>
      <div className="icon">
        <FaExclamationTriangle size={30} color="red" />
      </div>
      <div className="content">
        <div className="info">
          <span className="location">{location}</span>
          <span className="timestamp">{timestamp}</span>
        </div>
        <p className="message">{message}</p>
      </div>
    </div>
  );
};

export default NotificationCard;
