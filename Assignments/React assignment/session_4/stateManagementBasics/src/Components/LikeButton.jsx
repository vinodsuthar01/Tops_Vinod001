import React, { useState } from 'react'

function LikeButton() {
    const [count,setCount] = useState(0);

    
  return (
    <div>
        <h4>Like button</h4>
        <div className='likebtn' onClick={()=>setCount(count+1)}>{count} &#10084;</div>

    </div>  )
}

export default LikeButton