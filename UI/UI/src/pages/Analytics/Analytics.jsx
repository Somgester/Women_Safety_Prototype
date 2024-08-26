import React from 'react'
import "./analytics.css"

import Barchart from '../../components/Charts/BarChart.jsx'
import Piechart from '../../components/Charts/Piechart.jsx'
import Linechart from '../../components/Charts/Linechart.jsx'
const Analytics = () => {
  return (
    <div className='analytic'>
       
        <h1>Analytics</h1>


        <Barchart/>
        <Piechart />
        <Linechart />


      
    </div>
  )
}

export default Analytics
