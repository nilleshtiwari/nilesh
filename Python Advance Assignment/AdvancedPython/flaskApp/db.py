import sqlite3

import click
from flask import current_app, g

"""The first thing to do when working with a SQLite database (and most other Python database libraries)
 is to create a connection to it.
 Any queries and operations are performed using the connection, which is closed after the work is finished.

In web applications this connection is typically tied to the request. It is created at some point when handling a request,
 and closed before the response is sent."""


def get_db():
    """Setting up the connection with the database at the time of the request being made by the user"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


'''before_request
The before_request decorator allows us to execute a function before any request. i.e, the 
function defined with the .before_request() decorator will execute before every request is made.

flask --app flaskr init-db'''