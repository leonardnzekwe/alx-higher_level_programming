#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if both the URL and the file path are provided as arguments
if (process.argv.length === 4) {
  const url = process.argv[2];
  const filePath = process.argv[3];

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    } else {
    // Write the body response to the specified file in UTF-8 encoding
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
