#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

//  'request' module to perform an HTTP GET request to the Star Wars API URL.
request(apiUrl, function (error, response, body) {
  // Checks if there was no error during the HTTP request
  if (!error && response.statusCode === 200) {
    // Parses the JSON response bod
    const movieData = JSON.parse(body);
    // creates array of promises that fetch the data for each individual character.
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        // Uses another 'request' to fetch the data for the individual character.
        request(characterUrl, function (charError, charResponse, charBody) {
          // Checks if there was no error during the HTTP request
          if (!charError && charResponse.statusCode === 200) {
            // Parses the JSON response body
            const characterData = JSON.parse(charBody);
            // Resolves promise with the name of the character.
            resolve(characterData.name);
          } else {
            // rejects promise with the error message if  there was an error during the HTTP request
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
