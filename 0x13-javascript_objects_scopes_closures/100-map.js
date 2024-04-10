#!/usr/bin/node
const prevList = require('./100-data').list;
const newList = prevList.map(function (element, elementIndex) {
  return element * elementIndex;
});
console.log(prevList);
console.log(newList);
