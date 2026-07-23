import "./App.css";

import TrendingSongs from "./Components/TrendingSongs";
import IPLScoreFetcher from "./Components/IPLScoreFetcher";
import MovieSuggestions from "./Components/MovieSuggestions";
import AutoFetchData from "./Components/AutoFetchData";

function App() {
  return (
    <>
      <TrendingSongs />

      <IPLScoreFetcher />

      <MovieSuggestions />

      <AutoFetchData />
    </>
  );
}

export default App;