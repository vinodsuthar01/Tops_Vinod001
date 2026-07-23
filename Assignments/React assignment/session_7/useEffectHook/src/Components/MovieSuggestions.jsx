import { useEffect, useState } from "react";

function MovieSuggestions() {

    const [movies, setMovies] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetch("https://jsonplaceholder.typicode.com/users")
            .then((response) => response.json())
            .then((data) => {

                setMovies(data);

                setLoading(false);

            });

    }, []);

    return (

        <div className="card">

            <h2>Movie Suggestions</h2>

            {
                loading ?

                    <h3>Loading...</h3>

                    :

                    <ul>

                        {
                            movies.map((movie) => (
                                <li key={movie.id}>
                                    {movie.name}
                                </li>
                            ))
                        }

                    </ul>

            }

        </div>

    );
}

export default MovieSuggestions;