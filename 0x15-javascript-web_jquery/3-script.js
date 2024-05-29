#!/usr/bin/node
/* script adds the class, named red to the header element when user click on the tag DIV#red_header */
$('DIV#red_header').on('click', function () {
  $('header').addClass('red');
});
