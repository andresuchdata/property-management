# Property Management App

# Property Management App

This is a Flask-based property management application.

## Setup

1. Create a virtual environment and install dependencies:
   ```
   make install
   ```

2. Set up the database:
   ```
   make setup-db
   ```

3. Run the application:
   ```
   make run
   ```

Alternatively, you can run the setup (install and setup-db) and run (run) the application with:

```
make setup
make run
```

## Database Management

- To reset the database:
  ```
  make db-reset
  ```

- To set up the database with custom number of users and properties:
  ```
  flask db-setup <num_users> <num_properties>
  ```

## Testing

- To run tests:
  ```
  make test
  ```

## Cleanup

- To clean up generated files and virtual environment:
  ```
  make clean
  ```

## Project Structure

- `app/`: Contains the main application code
  - `extensions.py`: Initializes Flask extensions (SQLAlchemy, Migrate)
  - `commands.py`: Defines custom Flask commands for database management
  - `users/`, `properties/`, `rentals/`, `payments/`: Blueprint modules for different entities
- `scripts/`: Contains utility scripts
  - `db.py`: Defines functions for database setup and seeding
- `config.py`: Configuration settings for the application
- `Makefile`: Defines common tasks and commands for the project