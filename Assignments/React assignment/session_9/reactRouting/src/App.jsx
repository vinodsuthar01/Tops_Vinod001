import { Routes, Route } from "react-router-dom";

import Navbar from "./Pages/Navbar";

import HomePage from "./Pages/HomePage";
import DealsPage from "./Pages/DealsPage";
import CartPage from "./Pages/CartPage";
import NotFound from "./Pages/NotFound";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<HomePage />} />

        <Route path="/deals" element={<DealsPage />} />

        <Route path="/cart" element={<CartPage />} />

        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;