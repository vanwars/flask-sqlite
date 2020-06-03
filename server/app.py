# first install dependencies:
# pip install flask
# pip install -U flask-cors


# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

from flask import Flask
from flask import g
from flask import request
from flask_cors import CORS
import dbhelpers
import json


# initialize app:
app = Flask(__name__)
CORS(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    return 'Hi Vanessa!'

@app.route('/albums', methods=['GET', 'POST'])
def get_albums():
    if request.method == 'POST':
        title = request.json.get('title')
        artist_id = request.json.get('artist_id')
        record_id = dbhelpers.modify_db(
            'INSERT INTO albums(Title, ArtistId) VALUES(?, ?)', 
            args=(title, artist_id)
        )
        return record_id
    else:
        records = dbhelpers.query_db(
            'SELECT AlbumId, Title, ArtistId  FROM albums'
        )
    return json.dumps(records)

@app.route('/albums/<id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def get_album(id):
    if request.method == 'DELETE':
        dbhelpers.modify_db(
            'DELETE FROM albums WHERE AlbumId = ?', 
            args=(id,)
        )
        return json.dumps({
            'message': '{id} has been deleted from the albums table'.format(id=id)
        })

    record = dbhelpers.query_db(
        '''
        SELECT AlbumId, Title, ArtistId FROM albums 
        WHERE AlbumId = ?
        ''', 
        args=(id,),
        one=True
    )
    return json.dumps(record)