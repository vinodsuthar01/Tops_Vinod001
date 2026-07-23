import "./App.css";
import MovieList from "./components/MovieList";
import AddPlaylist from "./components/AddPlaylist";
import RestaurantSearch from "./components/RestaurantSearch";
import AddComment from "./components/AddComment";

function App() {
  return (
    <div className="App">
      <MovieList />

      <hr />

      <AddPlaylist />

      <hr />

      <RestaurantSearch />

      <hr />

      <AddComment />
    </div>
  );
}

export default App;