import collections
from abc import ABC

from flask import current_app

from app.blueprints import get_blueprint_modules
from app.cli._base_cli import _BaseCli
from app.extensions import db
from app.utils import exists_attr_in_module
from app.utils import get_attr_from_module


class SeederCli(_BaseCli, ABC):
    @staticmethod
    def __get_seeder_instances(modules: list) -> dict:
        """Get Seeder instances."""
        seeders = {}
        for item in modules:
            if exists_attr_in_module(item, 'Seeder'):
                seeder_instance = get_attr_from_module(item, 'Seeder')
                seeders[seeder_instance.priority] = seeder_instance
        return seeders

    def __get_seeders(self) -> dict:
        """Get Blueprints via dynamic way."""
        seeder_modules = [
            f'{item}.tests.seeder' for item in get_blueprint_modules()
        ]
        return self.__get_seeder_instances(seeder_modules)

    def run_command(self):
        session = db.Session()
        try:
            seeders = self.__get_seeders()
            ordered_seeders = collections.OrderedDict(sorted(seeders.items()))
            for seed in ordered_seeders.values():
                seed()
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
            if current_app.config['TESTING'] is False:
                print(' Database seeding completed successfully.')
