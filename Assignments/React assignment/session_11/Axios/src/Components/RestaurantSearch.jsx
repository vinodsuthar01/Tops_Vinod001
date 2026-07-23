import { useEffect, useState } from "react";
import axios from "axios";

function RestaurantSearch() {
  const [restaurants, setRestaurants] = useState([]);
  const [search, setSearch] = useState("");

  useEffect(() => {
    axios
      .get("https://mocki.io/v1/570c5e5c-8c8b-4c1e-8c8b-4c1e8c8b4c1e")
      .then((res) => setRestaurants(res.data))
      .catch(() => console.log("API Error"));
  }, []);

  const filtered = restaurants.filter((item) =>
    item.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <h2>Restaurant Search</h2>

      <input
        type="text"
        placeholder="Search Restaurant"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {filtered.map((item, index) => (
        <p key={index}>{item.name}</p>
      ))}
    </div>
  );
}

export default RestaurantSearch;