import os
import tempfile

import pytest
from flaskApp import create_app
from flaskApp.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    """initializing the app with the factory function and pass the testing config"""
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """The client fixture calls app.test_client() with the application object created by the app fixture.
     Tests will use the client to make requests to the application without running the server."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """The runner fixture is similar to client. app.test_cli_runner() 
    creates a runner that can call the Click commands registered with the application."""
    return app.test_cli_runner()



class AuthActions(object):
    """make a POST request to the login view with the client.
    Rather than writing that out every time, you can write a class with methods to do that, 
    and use a fixture to pass it the client for each test.
    With the auth fixture, we can call auth.login() in a test to log in as the test user,
     which was inserted as part of the test data in the app fixture."""

    def __init__(self, client):
        self._client = client

    def login(self, email='test@gmail.com', password='1111'):
        return self._client.post(
            '/auth/login',
            data={'email_address': email, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)