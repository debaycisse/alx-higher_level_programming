#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  let bigNum = parseInt(process.argv[2]);
  for (let i = 3; !isNaN(parseInt(process.argv[i])); i++) {
    if (bigNum < parseInt(process.argv[i])) {
      bigNum = parseInt(process.argv[i]);
    }
  }
  let secBigNum = parseInt(process.argv[2]);
  for (let j = 3; !isNaN(parseInt(process.argv[j])); j++) {
    const curNum = parseInt(process.argv[j]);
    if (secBigNum < curNum && curNum !== bigNum) {
      secBigNum = curNum;
    }
  }
  console.log(secBigNum);
}
