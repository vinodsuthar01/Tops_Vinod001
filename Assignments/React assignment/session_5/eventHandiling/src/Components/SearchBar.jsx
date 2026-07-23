import React, { useState } from "react";

function SearchBar() {
  const [product, setProduct] = useState("");

  return (
    <div>
      <input
        type="text"
        placeholder="Search Product..."
        value={product}
        onChange={(e) => setProduct(e.target.value)}
      />

      <h3>Searching For: {product}</h3>
    </div>
  );
}

export default SearchBar;