import { useEffect } from "react";

function TrendingSongs() {

    useEffect(() => {
        console.log("Component Mounted");
    }, []);

    return (
        <div className="card">
            <h2>Trending Songs</h2>

            <p>Open browser console to see the message.</p>
        </div>
    );
}

export default TrendingSongs;