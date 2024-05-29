#!/usr/bin/node
/* script adds an li tag with 'Item' as its content to the ul tag when user clicks on the tag DIV#add_item */
$('DIV#add_item').on('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
