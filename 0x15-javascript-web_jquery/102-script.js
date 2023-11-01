// Wait for the document to be fully loaded
$(document).ready(function () {
  // Add a click event handler to the "Translate" button
  $('#btn_translate').click(function () {
    // Get the language code from the input field
    const languageCode = $('#language_code').val();

    // Make an AJAX GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Select the <div> with id "hello" and display the translation
      $('#hello').text(data.hello);
    });
  });
});
