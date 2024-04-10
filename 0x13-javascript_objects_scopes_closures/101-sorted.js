#!/usr/bin/node
const data = require('./101-data').dict;
const newData = {};
for (const [key, value] of Object.entries(data)) {
  if (value in newData) {
    newData[value].push(key);
  } else {
    newData[value] = [];
    newData[value].push(key);
  }
}
console.log(newData);
