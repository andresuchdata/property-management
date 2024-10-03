import random
import sys
import os
from config import Config

# Add the parent directory to sys.path to allow importing from the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils import database_exists, create_database

# Import your models
from app.users.models import User
from app.properties.models import Property, UnitType, UnitPeriod
from app.extensions import db

def generate_random_phone():
    return f"+62{random.randint(800000000, 899999999)}"

def generate_random_nik():
    return f"{random.randint(1000000000000000, 9999999999999999)}"

################################################################################
# DB related functions
################################################################################
# drop all tables, and handle in case database not exists
def drop_tables(db):
    try:
        db.drop_all()
        print("Tables dropped successfully.")
    except SQLAlchemyError as e:
        print(f"Error dropping tables: {str(e)}")

def create_database_if_not_exists():
    if not database_exists(Config.SQLALCHEMY_DATABASE_URI):
        create_database(Config.SQLALCHEMY_DATABASE_URI)
        print(f"Database created: {Config.SQLALCHEMY_DATABASE_URI}")
    else:
        print(f"Database already exists: {Config.SQLALCHEMY_DATABASE_URI}")

def create_tables(db):
    db.Model.metadata.create_all(db.engine)
    print("Tables created successfully.")

def seed_database(db, num_users=10, num_properties=20):
    session = db.session
    users = []
    for _ in range(num_users):
        user = User(
            first_name=f"FirstName{_}",
            last_name=f"LastName{_}",
            nik=generate_random_nik(),
            email=f"user{_}@example.com",
            phone=generate_random_phone(),
            is_active=False,
            profile_picture=f"https://ui-avatars.com/api/?name=FirstName+LastName&background=random"
        )
        user.set_password("password123@")
        users.append(user)
    
    session.add_all(users)

    properties = []
    for _ in range(num_properties):
        property = Property(
            name=f"Property {_}",
            unit_type=random.choice(list(UnitType)),
            unit_price=random.uniform(100000, 1000000),
            unit_period=random.choice(list(UnitPeriod)),
            address=f"Address {_}, City",
            images=["https://img.freepik.com/free-vector/beautiful-home_24877-50818.jpg",
                    "https://img.freepik.com/free-vector/beautiful-home_24877-50819.jpg",
                    "https://img.freepik.com/free-vector/beautiful-home_24877-50820.jpg",
                    "https://img.freepik.com/free-vector/beautiful-home_24877-50821.jpg",
                    "https://img.freepik.com/free-vector/beautiful-home_24877-50822.jpg",
                    ]
        )
        properties.append(property)
    
    session.add_all(properties)

    try:
        session.commit()
        print(f"Database seeded successfully with {num_users} users and {num_properties} properties")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error seeding database: {str(e)}")
    finally:
        session.close()

def setup_database(db, num_users=10, num_properties=20):
    try:
        print("Creating tables...")
        create_tables(db)
        print("Seeding database...")
        seed_database(db, num_users, num_properties)
        print("Database setup completed successfully.")
    except Exception as e:
        print(f"Error during database setup: {str(e)}")