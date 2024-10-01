from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

    return app
