// Build a mini Instagram-style verification badge logic: declare a variable followers and use a ternary operator to set a variable badge to 'Verified Creator' if followers is more than 1000, or 'Regular User' otherwise. Print the badge value.

let followers = 1001;

let badge;

if(followers<=1000){
    badge="verified";
}else{
    badge="regular";
}

console.log(badge);
