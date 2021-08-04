.PHONY: run component shell migrate migrate-rollback linter coverage coverage-html test test-parallel
VENV := venv

help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make COMMAND\033[36m\033[0m\n\n  A general utility script.\n\n  Provides commands to run the application, database migrations, tests, etc.\n  Next command start up the application:\n\n    \44 make run\n\nCommands:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-14s\033[0m \t%s\n", $$1, $$2 }' $(MAKEFILE_LIST)

run:  ## Run web server
	$(VENV)/bin/python3 manage.py runserver

component:  ## Create a component scaffolding
	$(VENV)/bin/flask component --name ${name}

shell:  ## Shell context for an interactive shell for this application
	$(VENV)/bin/flask shell

migrate:  ## Upgrade to a later database migration
	$(VENV)/bin/flask db upgrade

migrate-rollback:  ## Revert to a previous database migration
	$(VENV)/bin/flask db downgrade

seed:  ## Fill database with fake data
	$(VENV)/bin/flask seed

linter:  ## Analyzes code and detects various errors
	$(VENV)/bin/pre-commit run flake8 --all-files

coverage: ## Report coverage statistics on modules
	$(VENV)/bin/coverage report -m

coverage-html: ## Create an HTML report of the coverage of the files
	$(VENV)/bin/coverage html

test: ## Run tests
	$(VENV)/bin/coverage run -m unittest

test-parallel:  ## Run tests in parallel
	$(VENV)/bin/nosetests --processes=-1
