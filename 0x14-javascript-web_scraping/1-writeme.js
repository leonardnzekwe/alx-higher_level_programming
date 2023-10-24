#!/usr/bin/node

const fs = require('fs');

// Check if both the file path and the string to write are provided as arguments
if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const stringToWrite = process.argv[3];

  // Write the string to the file in utf-8 and handle errors
  fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}
