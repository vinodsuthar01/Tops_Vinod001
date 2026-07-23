import React, { useState } from 'react'

function SongVote() {
    const [vote,setVote] = useState(0)

    function upVote(){
         setVote(vote+1) 
    }

    function downVote(){
        if(vote>0){
            setVote(vote-1)
        }else{
            alert("Vote should not be Negetive")
        }
    }
  return (
    <div>
        <div className="song-card">
      <h2>🎵 Shape of You</h2>
      <p>Artist: Ed Sheeran</p>

      <div className="vote-section">
        <button className="vote-btn" onClick={upVote}>⬆️ Upvote</button>

        <span className="vote-count">{vote} Votes</span>

        <button className="vote-btn" onClick={downVote}>⬇️ Downvote</button>
      </div>
    </div>
    </div>
  )
}

export default SongVote