"""Public views functional tests."""

import pytest


@pytest.mark.usefixtures("db")
def test_visit_home_page(client):
    """Visit home page.

    Parameters
    ----------
    client : webtest.TestApp
        The test client instance.
    """
    response = client.get("/")
    assert "Hello World!" in response
