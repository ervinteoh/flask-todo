"""Test configurations.

This module defines all reusable fixtures to be used in all subsequent
tests. Parameters are ``setup`` and ``teardown`` functions in tests to
reduce duplicate code in similar tests. Please find more information in
the linked documentation below.

Notes
-----
This module contains reusable fixtures for every test type. In the
event that a fixture would only be used in a specific test type, please
include those in their respective conftest.
"""

import os

import pytest

from src import create_app
from src.extensions import db as _db


@pytest.fixture(name="app")
def fixture_app():
    """Flask application instance.

    Yields
    ------
    flask.app.Flask
        The application instance.
    """
    os.environ["FLASK_ENV"] = "testing"
    application = create_app()
    ctx = application.test_request_context()
    ctx.push()

    yield application

    ctx.pop()


@pytest.fixture(name="db")
def fixture_db(app):
    """Database instance.

    Parameters
    ----------
    app : flask.app.Flask
        The application instance.

    Yields
    ------
    flask_sqlalchemy.SQLAlchemy
        The database instance.
    """
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()
