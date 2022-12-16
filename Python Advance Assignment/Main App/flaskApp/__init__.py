from flask import Flask, render_template, request
import os
import sqlite3
from flask_wtf.csrf import CSRFProtect
from werkzeug.debug import DebuggedApplication


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="41bb32412b7421539cde2c58ec53a6d0daf6f4104cb311e310bc4b5bd1aa2651",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "Company.sqlite"), 
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskApp import db
    db.init_app(app)  # adding c CLI command to create the database
    from flaskApp import auth, engine, errors
    app.register_blueprint(auth.bp)  # registering the blueprint with the app
    app.register_blueprint(engine.bp)
    app.register_blueprint(errors.bp)
    app.add_url_rule("/", endpoint="index")
    

    
    return app