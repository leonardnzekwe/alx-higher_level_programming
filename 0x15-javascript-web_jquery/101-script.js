// Wait for the document to be fully loaded
$(document).ready(function () {
  // Function to add a new <li> element to the list
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  // Function to remove the last <li> element from the list
  $('#remove_item').click(function () {
    const list = $('ul.my_list');
    list.find('li:last').remove();
  });

  // Function to clear all <li> elements from the list
  $('#clear_list').click(function () {
    const list = $('ul.my_list');
    list.empty();
  });
});
