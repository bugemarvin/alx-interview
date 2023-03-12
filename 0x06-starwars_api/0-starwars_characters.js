#!/usr/bin/node
// finding characters of a movie
const request = require('request');
const myUrl = 'https://swapi-api.alx-tools.com/api/films/';
const myInputs = process.argv[2];
function myRequster () {
  request.get(myUrl + myInputs, (err, req, res) => {
    return new Promise((resolve, reject) => {
      if (err) {
        reject(err);
      }
      if (req.statusCode === 200) {
        const users = JSON.parse(res).characters;
        resolve(characters(users, 0));
      }
    });
  });
}

function characters (info, j) {
  for (; j < info.length; j++) {
    request.get(info[j], async (err1, req1, res1) => {
      if (err1) console.log(err1);
      if (req1.statusCode === 200) {
        console.log(await JSON.parse(res1).name);
      }
    });
  }
}
myRequster();
