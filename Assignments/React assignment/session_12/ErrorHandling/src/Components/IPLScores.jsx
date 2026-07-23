import { useEffect, useState } from "react";

function IPLScores() {
  const [teams, setTeams] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    const fetchScores = async () => {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/users"
        );

        if (response.status !== 200) {
          throw new Error("Error");
        }

        const data = await response.json();
        setTeams(data);
      } catch (err) {
        setError(true);
      }
    };

    fetchScores();
  }, []);

  return (
    <div className="card">
      <h2>IPL Scores</h2>

      {error ? (
        <p>Error loading scores</p>
      ) : (
        teams.map((team) => (
          <p key={team.id}>
            {team.name} - {Math.floor(Math.random() * 250)}/
            {Math.floor(Math.random() * 10)}
          </p>
        ))
      )}
    </div>
  );
}

export default IPLScores;