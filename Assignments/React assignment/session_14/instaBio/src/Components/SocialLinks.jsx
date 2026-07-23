function SocialLinks({ links, theme = "light" }) {
  return (
    <div className={`social-links ${theme}`}>
      {links.map((item, index) => (
        <a
          key={index}
          href={item.url}
          target="_blank"
          rel="noreferrer"
        >
          {item.name}
        </a>
      ))}
    </div>
  );
}

export default SocialLinks;