// Write a function isEligibleForDiscount(totalAmount) that returns true if the totalAmount is greater than or equal to 500, otherwise false. Test it with values 300 and 700.

function isEligibleForDiscount(totalAmount){
    if(totalAmount >= 500){
        return true;
    }else{
        return false;
    }
}

console.log(isEligibleForDiscount(Number(prompt("enter total amt: "))));

