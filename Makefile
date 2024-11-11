# Define variables
PYTHON := python3
VENV := venv
PROJECT_NAME := your_project_name

# Default target
all: run

# Create and activate virtual environment
venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "To activate, run: source $(VENV)/bin/activate"

# Install dependencies
install: venv
	@echo "Installing dependencies..."
	. $(VENV)/bin/activate && pip install -r requirements.txt

# Run the project
run: venv
	@echo "Running $(PROJECT_NAME)..."
	. $(VENV)/bin/activate && $(PYTHON) run.py

# Setup the database
setup-db: venv
	@echo "Setting up the database..."
	. $(VENV)/bin/activate && flask db-create
	. $(VENV)/bin/activate && flask db init
	. $(VENV)/bin/activate && flask db migrate
	. $(VENV)/bin/activate && flask db upgrade
	. $(VENV)/bin/activate && flask db-setup

# Run tests
test: venv
	@echo "Running tests..."
	. $(VENV)/bin/activate && pytest

# Setup the entire project
setup: install setup-db
	@echo "Project setup complete."

# Clean up generated files and virtual environment
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.pytest_cache' -delete

# Reset the database
db-reset: venv
	. $(VENV)/bin/activate && flask db-reset

# Run the project in production mode
prod:
	gunicorn run:app

.PHONY: all venv install run setup-db test setup clean prod