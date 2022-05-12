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

from src import settings, extensions, public


def create_app():
    """App factory function.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    config = settings.config[app.config["ENV"]]
    app.config.from_object(config())
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)

    return app


def register_extensions(app: Flask):
    """Register flask extensions.

    Args:
        app (Flask): The flask application instance.

    """
    extensions.bcrypt.init_app(app)
    extensions.db.init_app(app)
    extensions.csrf_protect.init_app(app)
    extensions.login_manager.init_app(app)
    extensions.migrate.init_app(app, extensions.db)


def register_blueprints(app: Flask):
    """Register Flask blueprints."""
    app.register_blueprint(public.routes.blueprint)


def register_shellcontext(app: Flask):
    """Register shell context objects.

    Args:
        app (Flask): The flask application instance.

    """
    shell_context = {"db": extensions.db}

    app.shell_context_processor(lambda: shell_context)
