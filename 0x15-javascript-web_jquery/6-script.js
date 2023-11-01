// Wait for the document to be fully loaded
$(document).ready(function () {
  // Select the <div> with id "update_header" and add a click event handler
  $('#update_header').click(function () {
    // Select the <header> element and update its text
    $('header').text('New Header!!!');
  });
});
