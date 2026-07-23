import { useEffect, useState } from "react";

function IPLScoreFetcher() {

    const [headline, setHeadline] = useState("");

    useEffect(() => {

        fetch("https://jsonplaceholder.typicode.com/posts")
            .then((response) => response.json())
            .then((data) => {
                setHeadline(data[0].title);
            });

    }, []);

    return (
        <div className="card">

            <h2>IPL Match Headline</h2>

            <h3>{headline}</h3>

        </div>
    );
}

export default IPLScoreFetcher;