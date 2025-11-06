let number = Math.floor(Math.random() * 100) + 1;
let user = 0;
let attempts = 0;

while (parseInt(user) !== number) {
    user = prompt("Please enter a number between 1 and 100:");
    let userNum = parseInt(user);

    if (!userNum && userNum !== 0) {
        alert("Input should be a number!");
        break;
    }

    if (number > userNum) {
        console.log("Random number is bigger");
    } else if (number < userNum) {
        console.log("Random number is less");
    }

    attempts++;

    if (userNum === number) {
        console.log("You won the game in " + attempts + " attempts");
        break;
    }
}
