import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import UserGreetings from './Components/UserGreetings'
import UserGreetingClass from './Components/UserGreetingClass'
import UserProfile from './Components/UserProfile'
import profileImg from './assets/portrait-handsome-hispanic-male-doctor-600nw-2608441611.webp'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Welcome To React JSX!</h1> 
    <UserGreetings username="vinod"/> 
    <UserGreetingClass user='Ram'  />  
    <UserProfile about="I am Heart Surgeon" profileImg={profileImg}/>
    </>
  )
}

export default App
