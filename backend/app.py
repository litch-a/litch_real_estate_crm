from flask import Flask
from extensions import db, migrate, jwt
from config import Config
from models import register_models

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    #Initialize extensions

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    #Register models

    register_models()

    #Registration of Blueprints

    return app

app=create_app()