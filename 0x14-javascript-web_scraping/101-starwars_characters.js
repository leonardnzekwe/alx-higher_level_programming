#!/usr/bin/node

const request = require('request');

// Check if a Movie ID is provided as an argument
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
        const characterUrls = movieData.characters;

        // Function to get character names from their URLs
        function getCharacterName (url) {
          return new Promise((resolve, reject) => {
            request(url, (error, response, body) => {
              if (error) {
                reject(new Error(error.message)); // Use an Error object as the rejection reason
              } else if (response.statusCode !== 200) {
                reject(new Error(`Failed to retrieve character data. Status code: ${response.statusCode}`));
              } else {
                const characterData = JSON.parse(body);
                resolve(characterData.name);
              }
            });
          });
        }

        // Fetch and print character names in the same order as in the `characters` array
        characterUrls.reduce((promise, characterUrl) => {
          return promise.then(() => {
            return getCharacterName(characterUrl).then((characterName) => {
              console.log(characterName);
            });
          });
        }, Promise.resolve());
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
}
