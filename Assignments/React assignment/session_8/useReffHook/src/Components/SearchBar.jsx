import { useEffect, useRef } from "react";

function SearchBar() {

  const inputRef = useRef();

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div className="card">

      <h2>Search Product</h2>

      <input
        type="text"
        placeholder="Search..."
        ref={inputRef}
      />

      <button>Search</button>

    </div>
  );
}

export default SearchBar;