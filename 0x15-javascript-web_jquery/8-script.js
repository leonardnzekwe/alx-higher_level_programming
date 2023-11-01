// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch movie data
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Select the <ul> with id "list_movies"
    const ulList = $('#list_movies');

    // Iterate through the movies in the response data and add them to the list
    data.results.forEach(function (movie) {
      const movieTitle = movie.title;
      // Create a new <li> element with the movie title and append it to the <ul>
      $('<li>').text(movieTitle).appendTo(ulList);
    });
  });
});
