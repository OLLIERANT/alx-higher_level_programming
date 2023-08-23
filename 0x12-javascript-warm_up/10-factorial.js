#!/usr/bin/node
// Define the factorial function
function factorial(n) {
	// Base case: factorial of 0 is 1
	// Factorial of NaN is 1
	if (n === 0 || isNaN(n)) {
		return 1;
	}
	// Recursive case: factorial(n) = n * factorial(n - 1)
	return n * factorial(n - 1);
}

// Get the argument passed to the script
const inputArgument = parseInt(process.argv[2]);

// Calculate the factorial using the factorial function
const result = factorial(inputArgument);

// Print the result
console.log(result);
