# encoding: utf-8
"""
Example RESTful API Server.
"""
from flask import Flask
from flask_restx import Api
from .models import db
import logging

api_v1 = Api(
    version='1.0',
    title="FLASK | Ski Conditions API",
    description=(
        "This is a FLASK REST API with the ability to shred some gnar."
    ),
    # Serve Swagger UI under the blueprint at /api/v1/swaggerui so the
    # blueprint root /api/v1/ can be used for a JSON index.
    doc='/swaggerui',
)

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    app: Flask = Flask(__name__, **kwargs)

    # Load the config file
    app.config.from_object('config.DevelopmentConfig')

    # Initialize extensions
    db.init_app(app)

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Start scheduler (if enabled) — import here to avoid circular imports
    if app.config.get('SCHEDULER_ENABLED'):
        try:
            from . import tasks
            tasks.init_scheduler(app)
        except Exception:
            logging.exception('Failed to initialize scheduler')

    # Initialize the modules
    from . import modules
    modules.init_app(app)

    return app