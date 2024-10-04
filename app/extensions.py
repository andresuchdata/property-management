from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# This is factory pattern for global db object used by domain models, e.g User, Property, etc

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)