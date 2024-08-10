# Define the virtual environment
VENV_DIR = venv

# Path to the Python interpreter within the virtual environment
PYTHON = $(VENV_DIR)/bin/python

# Path to the Streamlit executable within the virtual environment
STREAMLIT = $(VENV_DIR)/bin/streamlit

# Name of the main Streamlit application file
APP = src/app.py

# Command to run the Streamlit application
run:
	@echo "Activating the virtual environment and running Streamlit..."
	@$(STREAMLIT) run $(APP)

# Command to install dependencies
install:
	@echo "Installing dependencies in the virtual environment..."
	@$(PYTHON) -m pip install -r requirements.txt

# Command to create the virtual environment
venv:
	@echo "Creating the virtual environment..."
	python3 -m venv $(VENV_DIR)

# Clean temporary files and caches (optional)
clean:
	@echo "Cleaning up temporary files..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

# Command to run the CRUD script
crud:
	@echo "Running CRUD script..."
	@$(PYTHON) src/crud.py

.PHONY: run install venv clean crud
