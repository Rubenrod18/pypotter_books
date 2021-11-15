.PHONY: run component shell migrate migrate-rollback linter coverage coverage-html test test-parallel
VENV := venv

help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make COMMAND\033[36m\033[0m\n\n  A general utility script.\n\n  Provides commands to run the application, database migrations, tests, etc.\n  Next command start up the application:\n\n    \44 make run\n\nCommands:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-14s\033[0m \t%s\n", $$1, $$2 }' $(MAKEFILE_LIST)

build:  ## Build Docker app
	docker-compose build --no-cache

run:  ## Run web server
	docker-compose up

component:  ## Create a component scaffolding
	docker-compose exec app flask component --name ${name}

shell:  ## Shell context for an interactive shell for this application
	docker-compose exec app flask shell

migrate:  ## Upgrade to a later database migration
	docker-compose exec app flask db upgrade

migrate-rollback:  ## Revert to a previous database migration
	docker-compose exec app flask db downgrade

seed:  ## Fill database with fake data
	docker-compose exec app flask seed

linter:  ## Analyzes code and detects various errors
	docker-compose exec app pre-commit run flake8 --all-files

coverage: ## Report coverage statistics on modules
	docker-compose exec app coverage report -m

coverage-html: ## Create an HTML report of the coverage of the files
	docker-compose exec app coverage html

test: ## Run tests
	docker-compose exec app coverage run -m unittest

test-parallel:  ## Run tests in parallel
	docker-compose exec app nosetests --processes=-1
