#!/usr/bin/node
const nTimes = parseInt(process.argv[2]);
if (isNaN(nTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nTimes; i++) {
    console.log('C is fun');
  }
}
