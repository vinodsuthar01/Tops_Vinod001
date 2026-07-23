import { useContext } from "react";
import UserContext from "../context/UserContext";

function Navbar() {
  const user = useContext(UserContext);

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "15px",
        background: "#2196f3",
        color: "white",
      }}
    >
      <h2>My Website</h2>

      <h3>
        {user.loggedIn
          ? `Welcome, ${user.username}`
          : "Please Login"}
      </h3>
    </div>
  );
}

export default Navbar;