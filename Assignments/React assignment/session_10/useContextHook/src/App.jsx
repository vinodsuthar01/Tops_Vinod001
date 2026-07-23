import { useState } from "react";

import UserContext from "./context/UserContext";
import ThemeContext from "./context/ThemeContext";
import NotificationContext from "./context/NotificationContext";

import Navbar from "./components/Navbar";
import Parent from "./components/Parent";
import Notifications from "./components/Notifications";

function App() {
  const [theme, setTheme] = useState("light");

  const [count, setCount] = useState(5);

  const user = {
    username: "Vinod",
    loggedIn: true,
  };

  const styles = {
    backgroundColor: theme === "light" ? "#ffffff" : "#1f1f1f",
    color: theme === "light" ? "#000" : "#fff",
    minHeight: "100vh",
    padding: "20px",
    transition: "0.3s",
  };

  return (
    <UserContext.Provider value={user}>
      <ThemeContext.Provider value={theme}>
        <NotificationContext.Provider value={{ count, setCount }}>
          <div style={styles}>
            <Navbar />

            <br />

            <button
              onClick={() =>
                setTheme(theme === "light" ? "dark" : "light")
              }
            >
              Switch to {theme === "light" ? "Dark" : "Light"} Theme
            </button>

            <hr />

            <Parent />

            <hr />

            <Notifications />
          </div>
        </NotificationContext.Provider>
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

export default App;