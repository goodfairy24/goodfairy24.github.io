function sayHello() {
    const name = prompt("what is your name?");
    alert("Hello, " + name + "! Welcome to my website.");
}

sayHello();

function rollDice() {
    let dice = Math.floor(Math.random() * 6) + 1;
    alert(" You have rolled a " + dice + "!");
}

rollDice();

function jobSearch() {
    let months = 0;
    let dice = Math.floor(Math.random() * 6) + 1;
    months += dice
    alert(" it will take you " + months + " months to get your first job ");
}

jobSearch();

function comfortLevel (html, css, js) {
    const average = (html + css + js) / 3;
    if (average >= 7) {
        alert("You are a pro");
    } else if (average >= 4) {
        alert("Don't worry you're nearly there!");
    } else {
        alert("Keep trying you will get there");
    }
}

comfortLevel(9, 7, 3);


function darkMode() {
    document.body.style.backgroundColor = 'black';
    document.body.style.color = 'white';
    document.body.style.backgroundImage = 'none';
    document.getElementById("#").style.color ='white';
}

function lightMode() {
    document.body.style.backgroundColor = 'white';
    document.body.style.Color = 'white';
    document.body.style.backgroundImage = 'linear-gradient(62deg,rgba(0, 0, 255, 0.367) 0%, rgba(183, 0, 255, 0.148) 100%)';
    document.getElementById("#").style.color ='black';
}