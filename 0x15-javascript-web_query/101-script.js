$(function () {
  // list
  const list = '<li>Item</li>';
  // add list
  $('div#add_item').click(function () {
    $('ul.my_list').append(list);
  });
  // remove list
  $('div#remove_item').click(function () {
    $('ul.my_list :last').remove();
  });
  // erase list
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
