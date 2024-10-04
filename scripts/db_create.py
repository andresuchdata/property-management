from sqlalchemy_utils import database_exists, create_database
from config import Config

def create_database_if_not_exists():
    if not database_exists(Config.SQLALCHEMY_DATABASE_URI):
        create_database(Config.SQLALCHEMY_DATABASE_URI)
        print(f"Database created: {Config.SQLALCHEMY_DATABASE_URI}")
    else:
        print(f"Database already exists: {Config.SQLALCHEMY_DATABASE_URI}")

if __name__ == "__main__":
    create_database_if_not_exists()