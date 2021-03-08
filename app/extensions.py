from flask import Flask
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
security = Security()
mail = Mail()
ma = Marshmallow()
api = Api(prefix='/api', title='Flask Api Alchemy')


def init_app(app: Flask):
    # Order matters: Initialize SQLAlchemy before Marshmallow
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    mail.init_app(app)
    api.init_app(app)
    _init_flask_security_too_app(app)


def _init_flask_security_too_app(flask_app: Flask):
    from app.blueprints.user.models import user_datastore
    security.init_app(flask_app, datastore=user_datastore,
                      register_blueprint=False)
