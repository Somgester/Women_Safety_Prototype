import React from 'react';
import "./notification.css";
import NotificationCard from '../../components/notification-card/NotificationCard';

const Notification = () => {
  
  const notifications = [
    {
      timestamp: "2024-08-20 14:35",
      location: "New York City",
      message: "Suspicious activity reported in Central Park."
    },
    {
      timestamp: "2024-08-20 12:20",
      location: "Los Angeles",
      message: "Attempted kidnapping near Sunset Boulevard."
    },
    {
      timestamp: "2024-08-20 09:15",
      location: "Chicago",
      message: "Emergency alert: stay indoors due to ongoing investigation."
    },
    {
      timestamp: "2024-08-20 09:15",
      location: "Chicago",
      message: "Emergency alert: stay indoors due to ongoing investigation."
    },
    {
      timestamp: "2024-08-20 09:15",
      location: "Chicago",
      message: "Emergency alert: stay indoors due to ongoing investigation."
    },
    {
      timestamp: "2024-08-20 09:15",
      location: "Chicago",
      message: "Emergency alert: stay indoors due to ongoing investigation."
    },
    {
      timestamp: "2024-08-20 09:15",
      location: "Chicago",
      message: "Emergency alert: stay indoors due to ongoing investigation."
    }
  ];

  return (
    <div className='notification'>
      <h1 style={{ fontSize: "30px", fontWeight: "bold" }}>Notifications & Alerts</h1>
      <div className="not-box">
        {notifications.map((notification, index) => (
          <NotificationCard
            key={index}
            timestamp={notification.timestamp}
            location={notification.location}
            message={notification.message}
          />
        ))}
      </div>
    </div>
  );
};

export default Notification;
