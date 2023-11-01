// Wait for the document to be fully loaded
$(document).ready(function () {
  // Select the <div> with id "add_item" and add a click event handler
  $('#add_item').click(function () {
    // Create a new <li> element with the text "Item"
    const newItem = $('<li>Item</li>');

    // Add the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });
});
