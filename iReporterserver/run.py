import os
from flask_restful import Api, Resource
from app import create_app

config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)
api = Api(app)


if __name__ == "__main__":
    app.run()
