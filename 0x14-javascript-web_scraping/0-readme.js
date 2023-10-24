#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided as an argument
if (process.argv.length === 3) {
  const filePath = process.argv[2];

  // Read the file in utf-8 and handle errors
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
