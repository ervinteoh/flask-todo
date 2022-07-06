"""Functional test configuration.

This module defines all reusable fixtures to be used in all subsequent
tests. Parameters are ``setup`` and ``teardown`` functions in tests to
reduce duplicate code in similar tests. Please find more information in
the linked documentation below.

Notes
-----
This module contains reusable fixtures only for __functional__ tests.
In the event that a fixture would only be used in another test type,
please include those in their respective conftest.
"""

import pytest
from flask import Flask
from webtest import TestApp


@pytest.fixture
def client(app: Flask):
    """WSGI test client.

    Parameters
    ----------
    app : flask.Flask
        The application instance.

    Returns
    -------
    webtest.TestApp
        The test app instance.
    """
    return TestApp(app)
