import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import LikeButton from './Components/LikeButton'
import LoginForm from './Components/LoginForm'
import PlaylistAdder from './Components/PlaylistAdder'
import SearchBar from './Components/SearchBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <LikeButton/>
      <SearchBar/>
      <LoginForm/>
      <PlaylistAdder/>
      
    </>
  )
}

export default App
