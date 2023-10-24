#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided as an argument
if (process.argv.length === 3) {
  const movieId = process.argv[2];
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    } else {
      try {
        const movieData = JSON.parse(body);
        console.log(movieData.title);
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
}
