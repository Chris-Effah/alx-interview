const axios = require('axios');

function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    return axios.get(url)
        .then(response => {
            const charactersUrls = response.data.characters;
            const characterRequests = charactersUrls.map(url => axios.get(url));
            return Promise.all(characterRequests);
        })
        .then(characterResponses => {
            return characterResponses.map(response => response.data.name);
        })
        .catch(error => {
            console.error(`Failed to fetch movie data: ${error}`);
            return [];
        });
}

if (process.argv.length !== 3) {
    console.log("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId)
    .then(characters => {
        characters.forEach(character => console.log(character));
    })
    .catch(error => {
        console.error(`Error: ${error}`);
    });
