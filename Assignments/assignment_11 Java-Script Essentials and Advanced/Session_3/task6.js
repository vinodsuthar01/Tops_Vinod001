// Build a function getBadge(followers) that returns 'Verified Creator ⭐' if followers is 1000 or more, otherwise returns 'Regular User'. Use the ternary operator to implement this logic.

let followers1 = 999;

let verified = followers1>= 1000 ? "verified creator" : "regular user"

console.log(verified);