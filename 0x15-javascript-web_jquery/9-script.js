// Make an AJAX GET request to fetch the translation
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  // Select the <div> with id "hello" and display the translation
  $('#hello').text(data.hello);
});
