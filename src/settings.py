"""Flask configuration settings.

This module defines the flask application configurations that will be
initialized as enviornment variables. Each environment type depend on the
`FLASK_ENV` environment variable defined.

"""
import os
from abc import ABC, abstractmethod
from contextlib import suppress

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
WORKING_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# Includes all generated files
TEMP_DIR = os.path.join(WORKING_DIR, "tmp")


class BaseConfig(ABC):
    """Base configuration for the application.

    The class can be initialized into the flask application configuration
    by the following example code::

        app.config.from_object(...)

    Note:
        This class is an abstract class that does not specify the current
        application environment.

    Attributes:
        SECRET_KEY (str): Protection against cookie data tampering.
        STATIC_FOLDER (str): Static folder location.
        SQLALCHEMY_TRACK_MODIFICATIONS (str): Disable SQLAlchemy warnings.
        TEMPLATES_FOLDER (str): Templates folder location.

    """

    # pylint: disable=too-few-public-methods, invalid-name

    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    STATIC_FOLDER = "static"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_FOLDER = "templates"

    def __init__(self):
        with suppress(FileExistsError):
            os.makedirs(TEMP_DIR)

    @property
    @abstractmethod
    def DATABASE_URI(self):
        """Database Uniform Resource Identifier(URI).

        This method is an abstract property to be used by
        `SQLALCHEMY_DATABASE_URI` property method below to initialize the
        database URI.

        .. _Configuration - Flask-SQLAlchemy Documention(2.x):
           https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

        """

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """SQLAlchemy Database Uniform Resource Identifier(URI).

        This method uses the `DATABASE_URI` abstract property to initialize
        the database URI for SQLAlchemy.

        .. _Configuration - Flask-SQLAlchemy Documention(2.x):
           https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

        """
        return f"sqlite:///{self.DATABASE_URI}"


class DevelopmentConfig(BaseConfig):
    """Development configuration for the application.

    This configuration is only initialized when the application is executed in
    development environment. You can achieve that by running this command in
    the terminal::

        $ export FLASK_ENV=development

    Attributes:
        DATABASE_URI (str): Database URI path.
        DEBUG (bool): Enable debug.
        LOGGING_LEVEL (int): Logging level.
        TESTING (bool): Enable testing.

    """

    DATABASE_URI = os.path.join(TEMP_DIR, "development.db")
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    """Testing configuration for the application.

    This configuration is only initialized when the application is executed in
    testing environment. You can achieve that by running this command in
    the terminal::

        $ export FLASK_ENV=testing

    Attributes:
        DATABASE_URI (str): Database URI path.
        DEBUG (bool): Enable debug.
        LOGGING_LEVEL (int): Logging level.
        TESTING (bool): Enable testing.
        WTF_CSRF_ENABLED (str): Disable CSRF protect.

    """

    DATABASE_URI = ":memory:"
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration for the application.

    This configuration is only initialized when the application is executed in
    production environment. You can achieve that by running this command in
    the terminal::

        $ export FLASK_ENV=production

    Attributes:
        DATABASE_URI (str): Database URI path.
        DEBUG (bool): Enable debug.
        LOGGING_LEVEL (int): Logging level.
        TESTING (bool): Enable testing.

    """

    DATABASE_URI = os.path.join(TEMP_DIR, "production.db")
    DEBUG = False
    TESTING = False


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
