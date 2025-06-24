VENV_NAME := .venv
PYTHON := $(VENV_NAME)/bin/python

pre-commit-init:
	@pre-commit install