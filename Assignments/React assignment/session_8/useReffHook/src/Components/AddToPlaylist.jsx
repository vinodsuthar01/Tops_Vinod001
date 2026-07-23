import { useRef, useState } from "react";

function AddToPlaylist() {

  const [song, setSong] = useState("");

  const [playlist, setPlaylist] = useState([]);

  const inputRef = useRef();

  function addSong(e) {

    e.preventDefault();

    if (song.trim() === "") return;

    setPlaylist([...playlist, song]);

    setSong("");

    inputRef.current.focus();

  }

  return (

    <div className="card">

      <h2>Add To Playlist</h2>

      <form onSubmit={addSong}>

        <input
          ref={inputRef}
          type="text"
          placeholder="Song Name"
          value={song}
          onChange={(e) => setSong(e.target.value)}
        />

        <button type="submit">
          Add
        </button>

      </form>

      <ul>

        {
          playlist.map((item, index) => (
            <li key={index}>{item}</li>
          ))
        }

      </ul>

    </div>

  );
}

export default AddToPlaylist;