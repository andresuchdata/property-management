from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)