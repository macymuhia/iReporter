from flask import Flask
from instance.config import app_config
from app.api.v1 import blueprint_v1
from app.api.v2 import blueprint_v2


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False
    app.register_blueprint(blueprint_v1)
    app.register_blueprint(blueprint_v2)
    return app
