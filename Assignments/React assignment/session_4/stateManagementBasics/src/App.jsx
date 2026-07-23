import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import LikeButton from './Components/LikeButton'
import CartItem from './Components/CartItem'
import SongVote from './Components/SongVote'
import RateStar from './Components/RateStar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <LikeButton/>
      <CartItem />
      <SongVote/>
      <RateStar/>
    </>
  )
}

export default App
