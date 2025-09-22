// Demonstrating scope, parameters, return values, and animation triggers

// Global scope variable
let box = document.getElementById("box");

/**
 * Function with parameter and return value
 * @param {string} newColor - The color to change the box to
 * @returns {string} The final color applied
 */
function changeBoxColor(newColor) {
  box.style.backgroundColor = newColor;
  return newColor; // return value
}

/**
 * Function to trigger animation
 */
function startAnimation() {
  // Local scope variable
  let finalColor = changeBoxColor("green"); // calling function with parameter

  console.log("Box color changed to:", finalColor); // verify return value

  // Remove animation class if it exists, then re-add to restart animation
  box.classList.remove("animate");
  void box.offsetWidth; // trick to reset animation
  box.classList.add("animate");
}