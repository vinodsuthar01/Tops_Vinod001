function ProfileCard({ name, image, bio }) {
  return (
    <div className="profile-card">
      <img src={image} alt={name} />

      <h2>{name}</h2>

      <p>{bio}</p>
    </div>
  );
}

export default ProfileCard;