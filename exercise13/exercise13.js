let convert = true;

function toLiters(gallons) {
    return gallons * 3.78541;
}

function toMiles(meters) {
    return meters * 0.000621371;
}

function toCelsius(fer) {
    return (fer - 32) * 5 / 9;
}

while (convert) {
    let userInput = window.prompt("Do you want to convert? (yes/no)");

    if (userInput === "no") {
        convert = false;
        console.log("Goodbye!");
        break;
    }

    if (userInput === "yes") {
        let type = window.prompt("Choose converter: liters, miles, or celsius").toLowerCase();
        let value = parseFloat(window.prompt("Please enter the value"));

        if (type === "liters") {
            console.log(value + " gallons = " + toLiters(value) + " liters");
        } else if (type === "miles") {
            console.log(value + " meters = " + toMiles(value) + " miles");
        } else if (type === "celsius") {
            console.log(value + "F = " + toCelsius(value) + "C");
        } else {
            console.log("Converter not supported");
        }
    }
}
