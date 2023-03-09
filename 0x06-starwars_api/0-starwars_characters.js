#!/usr/bin/node
// finding characters of a movie

const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, req, res) => {
  if (err) console.log(err);

  if (req.statusCode === 200) {
    const info = JSON.parse(res).characters;
    sortUsers(info, 0);
  }
});

function sortUsers (info, counts) {
  request(info[counts], (err1, req1, res1) => {
    if (err1) console.log(err1);

    if (req1.statusCode === 200) {
      const user = JSON.parse(res1).name;
      console.log(user);
      sortUsers(info, counts + 1);
    }
  });
}
