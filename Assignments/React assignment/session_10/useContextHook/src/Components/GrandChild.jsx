import { useContext } from "react";
import ThemeContext from "../context/ThemeContext";

function GrandChild() {
  const theme = useContext(ThemeContext);

  return (
    <div
      style={{
        padding: "20px",
        marginTop: "10px",
        background: theme === "light" ? "#eee" : "#444",
        color: theme === "light" ? "black" : "white",
      }}
    >
      <h3>Grand Child Component</h3>

      <p>Current Theme : {theme}</p>
    </div>
  );
}

export default GrandChild;