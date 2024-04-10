#!/usr/bin/node
const fileSystem = require('node:fs');
for (let i = 2; i < 4; i++) {
  fileSystem.readFile(process.argv[i], 'utf8', function (error, content) {
    if (error) {
      console.log(error);
    } else {
      fileSystem.appendFile(process.argv[4], content + '\n', function (error) {
        if (error) {
          console.log(error);
        }
      });
    }
  });
}
