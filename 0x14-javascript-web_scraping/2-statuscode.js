#!/usr/bin/node

const request = require('request');
// Imports the 'request' module.

request.get(process.argv[2])
// Uses the 'request' module to perform an HTTP GET request to the URL.

  .on('response', function (response) {
    // Sets up an event listener for the 'response' event emitted by the HTTP request.

    console.log(`code: ${response.statusCode}`);
    // Log the HTTP status code of the response to the console.
  });
