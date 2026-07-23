import React, { useState } from "react";

function LikeButton() {
  const [count, setCount] = useState(0);

  function handleLike() {
    setCount(count + 1);
  }

  return (
    <div>
      <button onClick={handleLike}>❤️ Like</button>
      <h2>Likes: {count}</h2>
    </div>
  );
}

export default LikeButton;