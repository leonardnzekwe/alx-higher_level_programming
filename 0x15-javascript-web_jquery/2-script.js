// Wait for the document to be fully loaded
$(document).ready(function () {
  // Select the <div> with id "red_header" and add a click event handler
  $('#red_header').click(function () {
    // Select the <header> element and change its text color to red
    $('header').css('color', '#FF0000');
  });
});
