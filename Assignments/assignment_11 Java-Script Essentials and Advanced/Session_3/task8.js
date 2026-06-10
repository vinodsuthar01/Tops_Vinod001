// Given a variable username, write a condition that checks if username is truthy, and if so, logs 'Welcome, [username]!', otherwise logs 'Guest Login'.<br><br><em><strong>Hint:</strong> Try with username = '', username = null, and username = 'Priya'.</em>

let username = '';

if(username){
    console.log(`welcome ${username}!`);
    
}else{
    console.log('guest login');
    
}