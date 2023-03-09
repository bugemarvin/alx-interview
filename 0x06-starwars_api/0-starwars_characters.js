#!/usr/bin/node
// finding characters of a movie

const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, req, res) => {
  if (err) console.log(err);

  if (req) {
    const info = JSON.parse(res).characters;

    for (const people of Object.keys(info)) {
      request(info[people], 0);
      request(info[people], (err1, req1, res1) => {
        if (err1) {
          console.log(err1);
        }

        if (req1) {
          const character = JSON.parse(res1).name;
          console.log(character);
        }
      });
    }
  }
});
