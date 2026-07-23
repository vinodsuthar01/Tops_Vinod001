import React from 'react'

function ProductCard(props) {
  return (
    <div style={{padding:"20px",marginBottom:"30px"}}>
        <h4 style={{textAlign:"center"}}>Simple product card with name or price</h4>
        <div className='product-card'>
            <p>{props.productName}</p>
            <p>&#8377; {props.productPrice} </p>
        </div>
    </div>
  )
}

export default ProductCard