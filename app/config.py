import os
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database

load_dotenv()  # This loads the variables from .env file

class Config:
    SQLALCHEMY_DATABASE_URI = f"{os.getenv('DB_DRIVER', 'mysql')}://{os.getenv('DB_USER', '')}:{os.getenv('DB_PASSWORD', '')}@{os.getenv('DB_HOST', '')}:{os.getenv('DB_PORT', '')}/{os.getenv('DATABASE_NAME', 'default_database')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    @classmethod
    def init_app(cls, app):
        pass