#!/usr/bin/node
/* script fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json and displays it in tag DIV#character */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (returnedData) {
      $('DIV#character').text(returnedData.name);
    }
  );
});
