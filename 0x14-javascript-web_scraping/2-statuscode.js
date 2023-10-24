#!/usr/bin/node

const request = require('request');

// Check if a URL is provided as an argument
if (process.argv.length === 3) {
  const url = process.argv[2];

  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
