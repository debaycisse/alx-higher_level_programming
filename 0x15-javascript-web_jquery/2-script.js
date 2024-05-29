#!/usr/bin/node
/* script changes the color of header when one clicks on a particular different element */
$('DIV#red_header').on('click', function () {
  $('header').css('color', '#FF0000');
});
