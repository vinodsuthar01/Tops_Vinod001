function OrderStatus({ isDelivered }) {
  return (
    <div className="card">

      <h2>Order Status</h2>

      <h3>
        {isDelivered
          ? "Order Delivered 🎉"
          : "Order on the way 🚚"}
      </h3>

    </div>
  );
}

export default OrderStatus;