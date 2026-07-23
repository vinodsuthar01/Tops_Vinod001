import "./App.css";
import IPLScores from "./Components/IPLScores";
import TrendingSongs from "./Components/TrendingSongs";


function App() {
  return (
    <div className="App">
      <TrendingSongs />

      <hr />

      <IPLScores />
    </div>
  );
}

export default App;