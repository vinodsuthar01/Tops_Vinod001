import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import ProductCard from './Components/ProductCard'
import ProfileCard from './Components/ProfileCard'

function App() {
  const [count, setCount] = useState(0)

  


  return (


    <>
      
      <ProductCard productName="Toothbrush" productPrice={550} />
      <ProfileCard img={heroImg} userName="Vinod Suthar" followers={223} />
    </>
  )
}

export default App
