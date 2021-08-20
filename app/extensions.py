from flask import Flask
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

from app import __author__
from app import __description__
from app import __project__
from app import __version__
from app.wrappers.custom_api import CustomApi
from config import Config

db = SQLAlchemy()
migrate = Migrate()
security = Security()
mail = Mail()
ma = Marshmallow()
api = CustomApi(
    prefix='/api',
    author=__author__,
    version=__version__,
    authorizations={
        'auth_token': {
            'type': 'apiKey',
            'in': 'header',
            'name': Config.SECURITY_TOKEN_AUTHENTICATION_HEADER,
        },
    },
    title=__project__,
    description=__description__,
)


def init_app(app: Flask):
    # Order matters: Initialize SQLAlchemy before Marshmallow
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    ma.init_app(app)
    mail.init_app(app)
    api.init_app(app)
    _init_flask_security_too_app(app)

    @app.teardown_request
    def teardown_request_context(exception):
        if not app.config['TESTING']:
            db.session.commit()


def _init_flask_security_too_app(flask_app: Flask):
    from app.blueprints.user.models import user_datastore

    security.init_app(
        flask_app, datastore=user_datastore, register_blueprint=False
    )
