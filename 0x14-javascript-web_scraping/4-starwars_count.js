#!/usr/bin/node

const request = require('request');

// Check if an API URL is provided as an argument
if (process.argv.length === 3) {
  const apiUrl = process.argv[2];
  const characterId = 18; // Character ID for Wedge Antilles
  let count = 0;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    } else {
      try {
        const movieData = JSON.parse(body);
        movieData.results.forEach((film) => {
          film.characters.forEach((character) => {
            if (character.includes(characterId)) {
              count += 1;
            }
          });
        });
        console.log(count);
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
}
