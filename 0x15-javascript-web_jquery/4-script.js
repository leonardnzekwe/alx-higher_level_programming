// Wait for the document to be fully loaded
$(document).ready(function () {
  // Select the <div> with id "toggle_header" and add a click event handler
  $('#toggle_header').click(function () {
    // Select the <header> element
    const header = $('header');

    // Toggle the classes "red" and "green" on the header element
    header.toggleClass('red green');
  });
});
