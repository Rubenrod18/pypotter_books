import logging

from flask import current_app

from app.blueprints.role.test.seed import RoleSeeder
from app.blueprints.user.tests.seed import UserSeeder
from app.extensions import db

logger = logging.getLogger(__name__)


def _get_seeders() -> list:
    return [
        RoleSeeder,
        UserSeeder,
    ]


def init_seed() -> None:
    session = db.Session()
    try:
        for seed in _get_seeders():
            seed()
        session.commit()
    except Exception as e:
        logger.debug(e)
        session.rollback()
        raise
    finally:
        session.close()
        if current_app.config['TESTING'] is False:
            print(' Database seeding completed successfully.')
