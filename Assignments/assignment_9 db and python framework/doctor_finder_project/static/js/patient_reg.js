function validateForm() {
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let email = document.getElementById("email").value;
    let error = document.getElementById("error");

    error.innerHTML = "";

    if (name === "") {
        error.innerHTML = "Name is required";
        return false;
    }

    if (age === "" || age <= 0) {
        error.innerHTML = "Enter valid age";
        return false;
    }

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if (!email.match(emailPattern)) {
        error.innerHTML = "Invalid email";
        return false;
    }

    return true;
}