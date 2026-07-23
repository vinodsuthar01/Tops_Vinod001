import { useState } from "react";
import axios from "axios";

function AddPlaylist() {
  const [name, setName] = useState("");
  const [desc, setDesc] = useState("");
  const [message, setMessage] = useState("");

  const submitHandler = async (e) => {
    e.preventDefault();

    await axios.post(
      "https://jsonplaceholder.typicode.com/posts",
      {
        playlist: name,
        description: desc,
      }
    );

    setMessage("Playlist Added Successfully");
    setName("");
    setDesc("");
  };

  return (
    <div>
      <h2>Add Playlist</h2>

      <form onSubmit={submitHandler}>
        <input
          type="text"
          placeholder="Playlist Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <br /><br />

        <textarea
          placeholder="Description"
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
        ></textarea>

        <br /><br />

        <button>Add</button>
      </form>

      <p>{message}</p>
    </div>
  );
}

export default AddPlaylist;