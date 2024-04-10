#!/usr/bin/node
exports.converter = function (base) {
  function calculateNum (num) {
    return num.toString(base);
  }
  return calculateNum;
};
