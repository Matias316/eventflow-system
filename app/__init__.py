from flask import Flask
from .services.db import db
from .services.in_memory import redis_client
from .apis.events import events_bp

def create_app(config_name="default"):
    app = Flask(__name__)
    
    # Dynamically load configuration for environment (development, testing or production)
    app.config.from_object(f"app.config.{config_name.capitalize()}Config")

    db.init_app(app)
    redis_client.init_app(app)

    app.register_blueprint(events_bp, url_prefix="/events")

    return app
