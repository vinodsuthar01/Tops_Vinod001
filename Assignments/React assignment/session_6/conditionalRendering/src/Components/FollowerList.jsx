function FollowerList({ followers }) {
  return (
    <div className="card">

      <h2>Followers</h2>

      {
        followers.length === 0
          ? (
            <h3>No followers yet</h3>
          )
          : (
            <ul>
              {followers.map((user, index) => (
                <li key={index}>{user}</li>
              ))}
            </ul>
          )
      }

    </div>
  );
}

export default FollowerList;