import click
from flask.cli import with_appcontext
from app.extensions import db
from scripts.db import drop_tables,seed_database, create_database_if_not_exists, create_tables, setup_database  # Import setup_database

@click.command('db-create')
@with_appcontext
def db_create():
    create_database_if_not_exists()

@click.command('db-reset')
@with_appcontext
def db_reset():
    """Reset the database: drop all tables, recreate, and seed."""
    click.echo('Resetting the database...')
    
    drop_tables(db)
    click.echo('Creating tables...')
    create_tables(db)  # Ensure this function creates the tables
    click.echo('Seeding database...')
    seed_database(db)  # Pass the db instance to seed_database
    
    click.echo('Database has been reset and seeded.')

@click.command('db-setup')
@click.argument('num_users', default=10)  # Optional argument for number of users
@click.argument('num_properties', default=20)  # Optional argument for number of properties
@with_appcontext
def db_setup(num_users, num_properties):
    """Setup the database: create tables and seed with data."""
    click.echo('Setting up the database...')
    setup_database(db, num_users, num_properties)  # Call the setup_database function
    click.echo('Database setup completed.')