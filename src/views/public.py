"""Public section, including homepage and signup."""

from flask import Blueprint, current_app

blueprint = Blueprint("public", __name__)


@blueprint.route("/")
@blueprint.route("/home")
def home():
    """Home Page."""
    current_app.logger.info("Hello from the home route!")
    current_app.logger.debug("Hello from the home route!")
    current_app.logger.warning("Hello from the home route!")
    current_app.logger.error("Hello from the home route!")
    current_app.logger.fatal("Hello from the home route!")
    return "Hello World!"
