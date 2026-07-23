import { useState } from "react";
import axios from "axios";

function AddComment() {
  const [username, setUsername] = useState("");
  const [comment, setComment] = useState("");
  const [response, setResponse] = useState(null);

  const submitHandler = async (e) => {
    e.preventDefault();

    const res = await axios.post(
      "https://jsonplaceholder.typicode.com/comments",
      {
        username,
        comment,
      }
    );

    setResponse(res.data);

    setUsername("");
    setComment("");
  };

  return (
    <div>
      <h2>Add Comment</h2>

      <form onSubmit={submitHandler}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <br /><br />

        <textarea
          placeholder="Comment"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
        ></textarea>

        <br /><br />

        <button>Submit</button>
      </form>

      {response && (
        <div>
          <h3>Response</h3>

          <p>ID : {response.id}</p>
          <p>Username : {response.username}</p>
          <p>Comment : {response.comment}</p>
        </div>
      )}
    </div>
  );
}

export default AddComment;