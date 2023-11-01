// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch character data
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character's name from the response data
    const characterName = data.name;

    // Select the <div> with id "character" and display the character name
    $('#character').text(characterName);
  });
});
