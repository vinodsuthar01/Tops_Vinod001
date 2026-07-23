import React, { useState } from 'react'

function RateStar() {

    const [myRate,setMyRate] = useState(0)
    
  return (

    <div className="rating-card">
      <h2>Rate this Restaurant</h2>

      <div className="star-section">
        <span className="star" onClick={()=>setMyRate(1)}>{myRate >= 1 ? "⭐":"☆"}</span>
        <span className="star" onClick={()=>setMyRate(2)}>{myRate >= 2 ? "⭐":"☆"}</span>
        <span className="star" onClick={()=>setMyRate(3)}>{myRate >= 3 ? "⭐":"☆"}</span>
        <span className="star" onClick={()=>setMyRate(4)}>{myRate >= 4 ? "⭐":"☆"}</span>
        <span className="star" onClick={()=>setMyRate(5)}>{myRate >= 5 ? "⭐":"☆"}</span>
      </div>

      <p>Your Rating: {myRate} / 5</p>
    </div>


  )
}

export default RateStar