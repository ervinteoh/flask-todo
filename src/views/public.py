"""Public views.

The views defined in this module are registered in the root path of the
application. This package are mainly for the web pages such as Home,
About and Contact pages.
"""

from flask import Blueprint, current_app

blueprint = Blueprint("public", __name__)


@blueprint.route("/home")
@blueprint.route("/")
def home():
    """Home Page."""
    current_app.logger.info("Hello from the home route!")
    current_app.logger.debug("Hello from the home route!")
    current_app.logger.warning("Hello from the home route!")
    current_app.logger.error("Hello from the home route!")
    current_app.logger.fatal("Hello from the home route!")
    return "Hello World!"
