#!/usr/bin/node
const arg = process.argv.slice(2);
const request = require('request');
const films = 'https://swapi-api.alx-tools.com/api/films';
const index = Number(arg[0]);
request(films, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const film = JSON.parse(body);
  const movies = film.results;
  for (const movie in movies) {
    const check = Number(movie) + 1;
    if (check === index) {
      // console.log(movies[movie].title);
      const characters = movies[movie].characters;
      for (const character in characters) {
        request(characters[character], function (err, res, body) {
          if (err) {
            console.log(err);
          }
          const person = JSON.parse(body);
          console.log(person.name);
        });
      }
    }
  }
});
