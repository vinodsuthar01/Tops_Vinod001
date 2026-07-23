

import { useRef, useState } from "react";

function FeedbackForm() {

  const [name, setName] = useState("");

  const [message, setMessage] = useState("");

  const messageRef = useRef();

  function handleSubmit(e) {

    e.preventDefault();

    alert("Feedback Submitted");

    setName("");
    setMessage("");

  }

  function focusMessage() {

    messageRef.current.focus();

  }

  return (

    <div className="card">

      <h2>Feedback Form</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <textarea
          ref={messageRef}
          rows="4"
          placeholder="Message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button type="submit">
          Submit
        </button>

      </form>

      <button onClick={focusMessage}>
        Focus Message
      </button>

    </div>

  );
}

export default FeedbackForm;