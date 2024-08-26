import Home from "./components/Home/Home.jsx"
import Sidebar from "./components/Sidebar/Sidebar.jsx"
import Navbar from "./components/navbar/Navbar.jsx"
const  App = () => {
  return (
    <div className="app">
      <Navbar />
      <Sidebar/>
      <Home />
       
       
    </div>
  )
}

export default App
