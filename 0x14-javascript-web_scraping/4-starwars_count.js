#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (body) {
    const data = JSON.parse(body);
    let counter = 0;
    for (const eachFilm in data.results) {
      const characters = data.results[eachFilm].characters;
      for (const eachCharacter in characters) {
        if (characters[eachCharacter].split('/').includes('18')) {
          ++counter;
          break;
        }
      }
    }
    console.log(counter);
  }
});
