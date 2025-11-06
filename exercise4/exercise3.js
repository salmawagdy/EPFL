let favoriteDishes = ["Pizza", "Sushi", "Pasta"];

console.log("My favorite dishes:");
for (let i = 0; i < favoriteDishes.length; i++) {
    console.log(favoriteDishes[i]);
}

console.log("Count: " + favoriteDishes.length);

favoriteDishes.push("Burger");

console.log("I have " + favoriteDishes.length + " favorite dishes.");

favoriteDishes.splice(1, 1);

favoriteDishes.sort();

console.log("Sorted favorite dishes: " + favoriteDishes);

console.log("Final count: " + favoriteDishes.length);
