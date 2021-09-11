from flask import Flask

from .config import configure_app

def create_app(config=None):
    import_name = __name__.split(".")[0]

    app = Flask(import_name)

    configure_app(app, import_name, config)

    return app