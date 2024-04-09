#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const reverseList = [];
  while (len > 0) {
    reverseList.push(list[--len]);
  }
  return reverseList;
};
