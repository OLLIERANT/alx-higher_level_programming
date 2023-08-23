#!/usr/bin/node
const firstArgument = process.argv[2];

// Convert the first argument to an integer
const intValue = parseInt(firstArgument);

// Check if the conversion was successful
if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
