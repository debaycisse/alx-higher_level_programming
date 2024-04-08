#!/usr/bin/node
function factorial (num) {
  if (!isNaN(num)) {
    if (num === 0) {
      return 1;
    } else {
      return (num * factorial(num - 1));
    }
  } else {
    return 1;
  }
}
console.log(factorial(parseInt(process.argv[2])));
