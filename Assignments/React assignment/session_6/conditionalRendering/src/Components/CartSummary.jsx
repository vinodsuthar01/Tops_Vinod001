function CartSummary({ cart }) {

  return (
    <div className="card">

      <h2>Cart Summary</h2>

      {
        cart.length === 0
          ? (
            <h3>Cart is empty</h3>
          )
          : (
            <>
              <ul>

                {
                  cart.map((item, index) => (
                    <li key={index}>
                      {item.name} - ₹{item.price}
                    </li>
                  ))
                }

              </ul>

              {
                cart.length >= 3 &&
                <button>Checkout Now</button>
              }

            </>
          )
      }

    </div>
  );
}

export default CartSummary;