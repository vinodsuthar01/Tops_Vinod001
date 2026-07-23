import React, { useState } from "react";

function PlaylistAdder() {
  const [song, setSong] = useState("");
  const [artist, setArtist] = useState("");

  const [playlist, setPlaylist] = useState([]);

  function handleSubmit(e) {
    e.preventDefault();

    

    const newSong = {
      song,
      artist,
    };

    setPlaylist([...playlist, newSong]);

    setSong("");
    setArtist("");
  }

  return (
    <div>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          placeholder="Song Name"
          value={song}
          onChange={(e) => setSong(e.target.value)}
        />

        <br /><br />

        <input
          type="text"
          placeholder="Artist"
          value={artist}
          onChange={(e) => setArtist(e.target.value)}
        />

        <br /><br />

        <button>Add Song</button>

      </form>

      <hr />

      <h2>Playlist</h2>

      {
        playlist.map((item, index) => (
          <div key={index}>
            🎵 {item.song} - {item.artist}
          </div>
        ))
      }

    </div>
  );
}

export default PlaylistAdder;