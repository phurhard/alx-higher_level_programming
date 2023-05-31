$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (i, movie) {
    $('ul#list_movies').append($('<li></li>')).text(movie.title);
  });
});
