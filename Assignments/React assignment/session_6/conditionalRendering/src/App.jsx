import "./App.css";

import Playlist from "./Components/Playlist";
import OrderStatus from "./Components/OrderStatus";
import FollowerList from "./Components/FollowerList";
import CartSummary from "./Components/CartSummary";

function App() {

  const songs = [
    { title: "Shape of You", artist: "Ed Sheeran" },
    { title: "Believer", artist: "Imagine Dragons" },
    { title: "Perfect", artist: "Ed Sheeran" },
  ];

  const followers = ["vinod", "rahul", "aman", "priya"];

  const cart = [
    { name: "Laptop", price: 55000 },
    { name: "Mouse", price: 800 },
    { name: "Keyboard", price: 1200 },
  ];

  return (
    <>
      <Playlist songs={songs} />

      <OrderStatus isDelivered={true} />

      <FollowerList followers={followers} />

      <CartSummary cart={cart} />
    </>
  );
}

export default App;