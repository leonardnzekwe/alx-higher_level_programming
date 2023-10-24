#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length === 3) {
  const apiUrl = process.argv[2];

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    } else {
      try {
        const todos = JSON.parse(body);

        // Create an object to store the count of completed tasks by user ID
        const completedTasksByUser = {};

        todos.forEach((todo) => {
          if (todo.completed) {
            if (completedTasksByUser[todo.userId]) {
              completedTasksByUser[todo.userId]++;
            } else {
              completedTasksByUser[todo.userId] = 1;
            }
          }
        });

        console.log(completedTasksByUser);
      } catch (parseError) {
        console.error(parseError);
      }
    }
  });
}
