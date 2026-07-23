import "./App.css";
import ProfileCard from "./components/ProfileCard";
import SocialLinks from "./components/SocialLinks";
import ProjectCard from "./components/ProjectCard";

function App() {
  const socialLinks = [
    {
      name: "GitHub",
      url: "https://github.com/vinodsuthar01",
    },
    {
      name: "LinkedIn",
      url: "https://www.linkedin.com/in/vinod-suthar-88715135b/",
    },
    {
      name: "Instagram",
      url: "https://instagram.com/suthar_v_01",
    },
  ];

  return (
    <div className="container">
      <ProfileCard
        name="Vinod Suthar"
        image="https://i.pravatar.cc/200?img=12"
        bio="Full Stack Python Developer | React | Django | REST API | Passionate about building modern web applications."
      />

      <SocialLinks links={socialLinks} theme="dark" />

      <h2 className="heading">My Projects</h2>

      <div className="project-section">
        <ProjectCard
          title="Furniture E-Commerce"
          description="A complete furniture shopping website built using React and Django with authentication and cart."
          image="https://picsum.photos/300/180?1"
          github="https://github.com/vinodsuthar01/furniture_web_app"
          demo="https://example.com"
        />

        <ProjectCard
          title="Site Manager ERP"
          description="ERP system to manage workers, attendance, expenses and reports."
          image="https://picsum.photos/300/180?2"
          github="https://github.com/vinodsuthar01/siteRecordManager"
          demo="https://example.com"
        />

        <ProjectCard
          title="Task Manager"
          description="Responsive portfolio website developed using React."
          image="https://picsum.photos/300/180?3"
          github="https://github.com/vinodsuthar01/task_manager"
          demo="https://example.com"
        />
      </div>
    </div>
  );
}

export default App;