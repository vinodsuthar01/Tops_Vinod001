import React from 'react'

function ProfileCard({img="",
    username="username",
    followers=0,
}) {
  return (
    <div>
        <h4 style={{textAlign:"center"}}>Simple Profile card Using Props</h4>

        <div className="profile-card">
            <div className="profile-item">
                <img src={img} alt="profile-img" />
            </div>
            <div className="profile-item">
                <div className="title">{username}</div>
                <div className="info">{followers} followers</div>
                <div className="info"><p>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</p></div>
            </div>

        </div>
    </div>
  )
}

export default ProfileCard