#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmApiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let characterUrls = [];
const characterNames = [];

const fetchCharacterUrls = async () => {
  await new Promise(resolve => request(filmApiUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching film: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const responseBody = JSON.parse(body);
      characterUrls = responseBody.characters;
      resolve();
    }
  }));
};

const fetchCharacterNames = async () => {
  if (characterUrls.length > 0) {
    for (const url of characterUrls) {
      await new Promise(resolve => request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
          console.error('Error fetching character: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const responseBody = JSON.parse(body);
          characterNames.push(responseBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No characters found');
  }
};

const displayCharacterNames = async () => {
  await fetchCharacterUrls();
  await fetchCharacterNames();

  characterNames.forEach((name, index) => {
    if (index === characterNames.length - 1) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  });
};

displayCharacterNames();
