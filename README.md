# flask-sqlite

## Step 1: Install Dependencies
Install the Python dependencies using pip
```bash
$ pip install flask
$ pip install -U flask-cors
```

## Step 2: Run the Server
Navigate into the server directory and run the flask app from the command line:

```bash
$ cd server
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

Then navigate to: <a href="http://127.0.0.1:5000/" target="_blank">http://127.0.0.1:5000/</a>. This is the API that you can modify to interact with your database.

Finally, open `client/index.html` in your web browser in order to interact with your server.
