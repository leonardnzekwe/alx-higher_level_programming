#!/usr/bin/node

const request = require('request');

// Check if an API URL is provided as an argument
if (process.argv.length === 3) {
  const apiUrl = process.argv[2];
  const characterId = 18; // Character ID for Wedge Antilles

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    } else {
      try {
        const movieData = JSON.parse(body);
        const moviesWithWedge = movieData.results.filter(movie =>
          movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );
        console.log(moviesWithWedge.length);
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
}
