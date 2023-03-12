#!/usr/bin/node
// finding characters of a movie

const { info } = require('console');
const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], async (err, req, res) => {
  if (err) throw err;

  if (req.statusCode === 200) {
    const info = JSON.parse(res).characters;
    await sortOrder(info, 0);
  }
});

function sortOrder (info, character) {
  for (character of info) {
    request.get(character, async (err1, req1, res1) => {
      if (err1) throw err1;
      if (req1.statusCode === 200) {
        const user = JSON.parse(res1).name;
        await console.log(user);
      }
    });
  }
}
