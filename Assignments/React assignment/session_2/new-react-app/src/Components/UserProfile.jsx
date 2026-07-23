import React from 'react'

function UserProfile(props) {
  return (
    <div>
        <h3 style={{textAlign:"center"}}>Profile Card</h3>
        <div className='profile-container'>
        
        <div className="profile-card">
            <img src={props.profileImg} alt="profile pic" />
            <p><strong>About</strong>: {props.about}</p>
        </div>
    </div>
    </div>
  )
}

export default UserProfile