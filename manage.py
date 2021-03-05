import os

from dotenv import load_dotenv

from app import create_app
from app.blueprints.base.test.seed import init_seed
from app.extensions import db

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG'))


@app.cli.command('seed', help='Fill database with fake data.')
def seeds() -> None:
    """Command line script for filling database with fake data."""
    init_seed()


@app.shell_context_processor
def make_shell_context() -> dict:
    """Returns the shell context for an interactive shell for this application.
    This runs all the registered shell context processors.

    To explore the data in your application, you can start an interactive Python
    shell with the shell command. An application context will be active,
    and the app instance will be imported.

    Example
    -------
    >>> source venv/bin/activate
    >>> flask shell

    References
    ----------
    Open a Shell: https://flask.palletsprojects.com/en/1.1.x/cli/#open-a-shell

    Returns
    -------
    dict
        Imports available in Python shell.

    """
    return {'app': app, 'db': db}


if __name__ == '__main__':
    app.run()
