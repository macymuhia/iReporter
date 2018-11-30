import os
from app import create_app
from app.api.v1 import blueprint

config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run()
