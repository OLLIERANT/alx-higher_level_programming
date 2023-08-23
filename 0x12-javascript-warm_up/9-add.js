#!/usr/bin/node
//define the add function
function add(a, b) {
	return a + b;
}

//get the first and second arguments passed to the script
const firstargument = parseInt(process.argv[2]);
const secondargument = parseInt(process.argv[3]);

//calculate the addition using the add function
const result = add(firstargument, secondargument);

//print the result
console.log(result);
