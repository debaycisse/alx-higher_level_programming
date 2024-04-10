#!/usr/bin/node
const fileSystem = require('node:fs');

const fileSources = [process.argv[2], process.argv[3], process.argv[4]];

for (let i = 0; i < 2; i++) {
  fileSystem.readFile(fileSources[i], 'utf8', function (error, content) {
    if (error) {
      console.log(error);
    } else {
      fileSystem.appendFile(fileSources[2], content + '\n', function (error) {
        if (error) {
          console.log(error);
        }
      });
    }
  });
}
