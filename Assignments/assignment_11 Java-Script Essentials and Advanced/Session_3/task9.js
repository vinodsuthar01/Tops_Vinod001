// Write a function isTruthy(input) that takes any value and return 'Truthy' or 'Falsy' based on JavaScript's truthy/falsy evaluation. Test it with '', 0, null, 'hello', and 42.<br><br><em><strong>Constraint:</strong> Do not use if-else; use the ternary operator.</em>


function isTruthy(input){
    let result = input ? true : false;
    console.log(result);  
}

isTruthy('');
isTruthy(null);
isTruthy(42);
isTruthy("hello")
