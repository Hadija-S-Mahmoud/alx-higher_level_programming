#!/usr/bin/node

// Imports the 'request' module.
const request = require('request');

// Constructs a URL for the specific Star Wars film
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Uses the 'request' module to perform an HTTP GET request to the constructed URL.
request(url, function (error, response, body) {
  // logs title if successful, log error if not.
  console.log(error || JSON.parse(body).title);
});
