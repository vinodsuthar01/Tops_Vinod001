function Playlist({ songs }) {
  return (
    <div className="card">
      <h2>🎵 Spotify Playlist</h2>

      <ul>
        {songs.map((song, index) => (
          <li key={index}>
            <strong>{song.title}</strong> - {song.artist}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Playlist;