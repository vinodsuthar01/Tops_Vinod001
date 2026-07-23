import React, { useState } from 'react'

function CartItem() {

    const [qty,setQty] = useState(0);
  return (
    
        <div className="product-card">
      <h2 className="product-name">Product Name</h2>

      <div className="quantity-section">
        <button className="btn" onClick={()=>setQty(qty-1)}>-</button>

        <span className="quantity">{qty}</span>

        <button className="btn" onClick={()=>setQty(qty+1)}>+</button>
      </div>

      <button className="add-btn">Add to Cart</button>
    </div>
  )
}

export default CartItem