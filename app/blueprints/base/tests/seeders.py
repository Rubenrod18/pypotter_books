import logging

from flask import current_app

from app.blueprints import get_bp_paths
from app.extensions import db
from app.utils import get_attr_from_module

logger = logging.getLogger(__name__)


def _get_seeder_modules() -> list:
    """Get Seeder modules."""
    dirs = get_bp_paths()
    dirs.remove('app.blueprints.base')
    return [f'{item}.tests.seeder' for item in dirs]


def _get_seeder_instances(modules: list) -> list:
    """Get Seeder instances."""
    return [get_attr_from_module(item, 'Seeder') for item in modules]


def _get_seeders() -> list:
    """Get Blueprints via dynamic way."""
    bp_modules = _get_seeder_modules()
    return _get_seeder_instances(bp_modules)


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
