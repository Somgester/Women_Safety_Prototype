import React from 'react'
import {Routes, Route} from "react-router-dom"
import Dashboard from '../../pages/Dashboard/Dashboard.jsx'
import Notification from '../../pages/Notification/Notification.jsx'
import Analytics from '../../pages/Analytics/Analytics.jsx'
import "./home.css"
const Home = () => {
  return (
    <div className='home'>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/notifications" element={<Notification />} />

      </Routes>
    </div>
  )
}

export default Home
