import { useContext } from "react";
import NotificationContext from "../context/NotificationContext";

function Notifications() {
  const { count, setCount } = useContext(NotificationContext);

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Unread Messages : {count}</h2>

      <button
        onClick={() => setCount(count + 1)}
        style={{ marginRight: "10px" }}
      >
        Receive Message
      </button>

      <button
        onClick={() => setCount(0)}
      >
        Mark All Read
      </button>
    </div>
  );
}

export default Notifications;