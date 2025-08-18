from flask import Flask
from extensions import db, migrate, jwt, cors
from config import Config
from models import register_models
from routes import (
    auth_bp,
    property_bp,
    client_bp,
    lead_bp,
    agent_bp,
    transaction_bp,
    analytics_bp
)

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    #Initialize extensions

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    #Register models

    register_models()

    #Registration of Blueprints

    app.register_blueprint(property_bp, url_prefix="/properties")
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(lead_bp, url_prefix='/leads')
    app.register_blueprint(agent_bp, url_prefix='/agents')
    app.register_blueprint(transaction_bp, url_prefix='/transactions')
    app.register_blueprint(analytics_bp, url_prefix='/analytics')

    return app

app=create_app()