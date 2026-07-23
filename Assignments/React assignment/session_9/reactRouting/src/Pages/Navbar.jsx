import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav>

      <NavLink
        to="/"
        style={({ isActive }) => ({
          color: isActive ? "red" : "black",
        })}
      >
        Home
      </NavLink>

      <NavLink
        to="/deals"
        style={({ isActive }) => ({
          color: isActive ? "red" : "black",
        })}
      >
        Deals
      </NavLink>

      <NavLink
        to="/cart"
        style={({ isActive }) => ({
          color: isActive ? "red" : "black",
        })}
      >
        Cart
      </NavLink>

    </nav>
  );
}

export default Navbar;