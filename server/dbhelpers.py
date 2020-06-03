import sqlite3
from flask import g

DATABASE = 'chinook.db'

def row_to_dictionary(cursor, row):
    return dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row)
    )

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = row_to_dictionary # sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def modify_db(query, args=()):
    cur = get_db().execute(query, args)
    row_id = None
    if query.lower().find('insert'):
        row_id = cur.lastrowid
    cur.close()
    get_db().commit()
    return row_id
