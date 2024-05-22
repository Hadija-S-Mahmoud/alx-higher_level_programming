#!/usr/bin/node

// Imports the built-in Node.js 'fs' module
const fs = require('fs');

// Imports the 'request' module
const request = require('request');

// Uses 'request' module to perform HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
