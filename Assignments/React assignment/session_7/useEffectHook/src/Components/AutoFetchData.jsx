import { useEffect, useState } from "react";

function AutoFetchData() {

    const [posts, setPosts] = useState([]);

    useEffect(() => {

        fetch("https://jsonplaceholder.typicode.com/posts")
            .then((response) => response.json())
            .then((data) => {

                setPosts(data.slice(5,10));

            });

    }, []);

    return (

        <div className="card">

            <h2>Latest Posts</h2>

            <button>Fetch Data</button>

            <ul>

                {
                    posts.map((post) => (

                        <li key={post.id}>
                            {post.title}
                        </li>

                    ))
                }

            </ul>

        </div>

    );
}

export default AutoFetchData;