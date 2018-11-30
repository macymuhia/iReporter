from flask import Flask
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False  # allows url to be api/v1/users or api/v1/users/
    return app