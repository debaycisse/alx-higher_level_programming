#!/usr/bin/node
/* script fetches and lists the title for all movies by using this URL - https://swapi-api.alx-tools.com/api/films/?format=json */
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data) {
      const resList = data.results;
      $.each(resList, function (index, obj) {
        $('UL#list_movies').append('<li>' + obj.title + '</li>');
      });
    });
});
