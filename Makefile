PYTHON_VERSION = 3.13.2
VENV_NAME = versiontwo-venv

.PHONY: install

install:
	@echo "Checking for pyenv..."
	@if ! command -v pyenv >/dev/null 2>&1; then \
		echo "pyenv not installed."; \
		exit 1; \
	fi

	@echo "Checking for pyenv-virtualenv..."
	@if ! pyenv-virtualenv --help >/dev/null 2>&1; then \
		echo "pyenv-virtualenv not installed."; \
		exit 1; \
	fi

	@echo "Installing Python $(PYTHON_VERSION) with pyenv..."
	pyenv install -s $(PYTHON_VERSION)
	@echo "Creating virtualenv $(VENV_NAME)..."
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	@echo "Setting local pyenv version to $(VENV_NAME)..."
	pyenv local $(VENV_NAME)
	@echo "Installing project dependencies..."
	pip install -r requirements.txt
	@echo "Done. Virtualenv $(VENV_NAME) is ready."
