"""Flask application entrypoint.

This module defines the flask application factory functions which
creates the application instance. The factory pattern allows for a more
organized project structure and avoid circular imports. If the
application instance is needed in another module, use::

    from flask import current_app

There are multiple ways to run the flask application. Please follow the
following steps to start the application.

Example
-------
Execute these commands on a terminal to first initialize the required
environmental variables and run the application::

    $ export FLASK_APP=src:create_app()
    $ flask run

Notes
-----
There are more information explaning all the available environmental
variables in the `settings.py` module.
"""

from flask import Flask

from src import extensions, settings
from src.views import public


def create_app() -> Flask:
    """Application factory function.

    The application's configurations are dependent on the environmental
    variables `FLASK_ENV`. Please read `settings.py` for more
    information.

    Returns
    -------
    flask.app.Flask
        The Flask application instance.
    """
    app = Flask(__name__)
    config = settings.config[app.config["ENV"]]()
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    configure_logger(app, config)

    return app


def register_extensions(app: Flask):
    """Register Flask extensions.

    Parameters
    ----------
    app : flask.app.Flask
        The application instance.
    """
    extensions.bcrypt.init_app(app)
    extensions.db.init_app(app)
    extensions.csrf_protect.init_app(app)
    extensions.login_manager.init_app(app)
    extensions.migrate.init_app(app, extensions.db)


def register_blueprints(app: Flask):
    """Register Flask blueprints.

    Parameters
    ----------
    app : flask.app.Flask
        The application instance.
    """
    app.register_blueprint(public.blueprint)


def register_shellcontext(app: Flask):
    """Register shell context objects.

    This function registers the subsequent classes to be used in Flask
    command line interface.

    Parameters
    ----------
    app : flask.app.Flask
        The application instance.
    """
    shell_context = {"db": extensions.db}

    app.shell_context_processor(lambda: shell_context)


def configure_logger(app: Flask, config: settings.BaseConfig):
    """Configure logger.

    Parameters
    ----------
    app : flask.app.Flask
        The flask application instance.
    config : settings.BaseConfig
        The configuration settings.
    """
    app.logger.handlers.clear()
    app.logger.propagate = False
    app.logger.addHandler(config.console_handler)
    if config.file_handler:
        app.logger.addHandler(config.file_handler)
