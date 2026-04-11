function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addDoctor() {
    let name = document.getElementById("name").value;
    let spec = document.getElementById("spec").value;
    let loc = document.getElementById("loc").value;

    if(name == "" || spec == "" || loc == "") {
        alert("All fields required");
        return;
    }

    let csrftoken = getCookie('csrftoken');

    fetch('/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            name: name,
            specialization: spec,
            location: loc
        })
    }).then(() => location.reload());
}