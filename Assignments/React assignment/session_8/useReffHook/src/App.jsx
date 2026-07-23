import "./App.css";

import SearchBar from "./Components/SearchBar";
import LoginForm from "./Components/LoginForm";
import AddToPlaylist from "./Components/AddToPlaylist";
import FeedbackForm from "./Components/FeedbackForm";

function App() {
  return (
    <>
      <SearchBar />

      <LoginForm />

      <AddToPlaylist />

      <FeedbackForm />
    </>
  );
}

export default App;