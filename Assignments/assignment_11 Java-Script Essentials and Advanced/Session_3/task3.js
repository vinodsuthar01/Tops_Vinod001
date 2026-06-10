// Write a function showDiscountTag(price) that checks if a product's price is less than 500 using a comparison operator. If true, print 'Special Discount!'; otherwise, print 'Regular Price'.

function showDiscountTag(price){
    
    if(price < 500){
        console.log("special discount!");
        
    }else{
        console.log("regular price");
        
    }
}

showDiscountTag(Number(prompt("Enter Price: ")));