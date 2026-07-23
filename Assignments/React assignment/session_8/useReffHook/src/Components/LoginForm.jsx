import { useRef, useState } from "react";

function LoginForm() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const userRef = useRef();

  function handleLogin(e) {

    e.preventDefault();

    alert(`Username: ${username}\nPassword: ${password}`);

    setUsername("");
    setPassword("");

    userRef.current.focus();

  }

  return (

    <div className="card">

      <h2>Login Form</h2>

      <form onSubmit={handleLogin}>

        <input
          ref={userRef}
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit">
          Login
        </button>

      </form>

    </div>

  );
}

export default LoginForm;