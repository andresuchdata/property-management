import os
from flask import Flask
from config import Config
import pymysql
from dotenv import load_dotenv
from app.extensions import db, migrate
from .commands import db_create, db_reset, db_setup

load_dotenv()
pymysql.install_as_MySQLdb()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from app.users.routes import user_bp
    from app.properties.routes import property_bp
    from app.rentals.routes import rental_bp
    from app.payments.routes import payment_bp

    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(property_bp, url_prefix='/api')
    app.register_blueprint(rental_bp, url_prefix='/api')
    app.register_blueprint(payment_bp, url_prefix='/api')

    # Add custom commands for DB reset and seeding
    app.cli.add_command(db_setup)
    app.cli.add_command(db_create)
    app.cli.add_command(db_reset)
    return app
