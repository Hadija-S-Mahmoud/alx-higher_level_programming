#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read  contents of a file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    // If errors occur during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // If filee is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});
