"""Initialize Flask app."""
import logging

from flask import Flask

from src.app.config import Config
from src.app.rest.v1.api import api
from src.app.rest.v1.data_api import data_store

_log = logging.getLogger(__name__)


def create_app():
    """Construct the core application."""
    _log.info("start create the app.")

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    app.register_blueprint(api)
    app.register_blueprint(data_store, url_prefix="/data")

    return app
