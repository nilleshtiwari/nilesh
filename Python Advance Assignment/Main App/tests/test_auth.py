import pytest
from flask import g, session
from flaskApp.db import get_db
import datetime 

def test_login(client, auth):
    with client:
        response = auth.login()
        assert response.status_code == 400



def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session