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
    title="FLASK | FLASK-RESTPlus GeoAPI",
    description=(
        "This is a FLASK-RESPlus powered API with geospatial super power.\n\n"
        "Checkout more at https://gis-ops.com or https://github.com/gis-ops\n"
    ),
)

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    app: Flask = Flask(__name__, **kwargs)

    # Load the config file
    app.config.from_object('config.DevelopmentConfig')

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Initialize extensions
    db.init_app(app)

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