

function ProjectCard({
  title,
  description,
  image,
  github,
  demo,
}) {
  return (
    <div className="project-card">
      <img src={image} alt={title} />

      <h3>{title}</h3>

      <p>{description}</p>

      <div className="buttons">
        <a href={github} target="_blank" rel="noreferrer">
          GitHub
        </a>

        <a href={demo} target="_blank" rel="noreferrer">
          Live Demo
        </a>
      </div>
    </div>
  );
}

export default ProjectCard;