#!/usr/bin/env node
// finding characters of a movie

const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, req, res) => {
  if (err) console.log(err);

  const info = JSON.parse(res);

  for (const character of info.characters) {
    request.get(character, (err1, req1, res1) => {
      if (err) console.log(err);

      const names = JSON.parse(res1);
      console.log(names.name);
    });
  }
});
