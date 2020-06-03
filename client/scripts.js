const getAlbums = (e) => {
    fetch('http://localhost:5000/albums')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.querySelector('#results').innerHTML = JSON.stringify(data, null, 2);
        });
    e.preventDefault();
};
const createNewAlbum = (e) => {
    let title = prompt('Enter an Album Title', 'Some title');
    let artist_id = prompt('Enter an Artist Id', 275);
    fetch('http://localhost:5000/albums', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            artist_id: artist_id
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.querySelector('#results').innerHTML = JSON.stringify(data, null, 2);
    });
    e.preventDefault();
};


const deleteAlbum = (e) => {
    let album_id = prompt('Enter an Album Id to delete', 1);
    fetch('http://localhost:5000/albums/' + album_id, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.querySelector('#results').innerHTML = JSON.stringify(data);
    });
    e.preventDefault();
};


document.querySelector('#albums').onclick = getAlbums;
document.querySelector('#create-album').onclick = createNewAlbum;
document.querySelector('#delete-album').onclick = deleteAlbum;