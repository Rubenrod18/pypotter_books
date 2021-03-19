import logging

from flask import current_app

from app.blueprints import get_blueprint_modules
from app.extensions import db
from app.utils import get_attr_from_module, exists_attr_in_module

logger = logging.getLogger(__name__)


def _get_seeder_instances(modules: list) -> list:
    """Get Seeder instances."""
    seeders = []
    for item in modules:
        if exists_attr_in_module(item, 'Seeder'):
            seeders.append(get_attr_from_module(item, 'Seeder'))
    return seeders


def _get_seeders() -> list:
    """Get Blueprints via dynamic way."""
    seeder_modules = [f'{item}.tests.seeder'
                      for item in get_blueprint_modules()]
    return _get_seeder_instances(seeder_modules)


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
