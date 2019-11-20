from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
import inspect


db = SQLAlchemy()

def create_app():

    from app.routes import api
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    app.register_blueprint(api)
    return app


def import_model(model_name):

    from app.models.base import BaseModel

    imported_module = import_module(f"app.models.{model_name.lower()}")
    for attr in dir(imported_module):
        info = getattr(imported_module, attr)
        if inspect.isclass(info) and issubclass(info, BaseModel) and attr.lower() == model_name:
            return info
    return None