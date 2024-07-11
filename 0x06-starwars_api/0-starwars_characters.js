#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;

    function printCharacter (index) {
      if (index >= characters.length) {
        // All characters have been printed
        return;
      }

      const charUrl = characters[index];

      request(charUrl, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
          // Move to the next character
          printCharacter(index + 1);
        }
      });
    }

    // Start printing characters from the first one
    printCharacter(0);
  }
});
