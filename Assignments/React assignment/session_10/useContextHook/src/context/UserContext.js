import { createContext } from "react";

const UserContext = createContext({
  username: "Vinod",
  loggedIn: true,
});

export default UserContext;