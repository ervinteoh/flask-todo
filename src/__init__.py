"""Flask application entrypoint.

This module defines the flask application factory function which creates the
application. There are multiple ways to run the flask application. Please
follow the following steps to start the application.

Example:
    Execute these commands on a terminal to first initialize the required
    environmental variables and run the application::

        $ export FLASK_APP=src:create_app()
        $ flask run

.. _Quickstart - Flask Documentation:
   https://flask.palletsprojects.com/en/2.1.x/quickstart/

"""
from flask import Flask

from src import settings


def create_app():
    """App factory function.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(settings.config[app.config["ENV"]])
    app.url_map.strict_slashes = False

    return app
