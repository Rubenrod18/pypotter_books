import os
from abc import ABC

from app.cli._base_cli import _BaseCli
from config import Config


class ComponentCli(_BaseCli, ABC):
    @staticmethod
    def __create_packages(component_name):
        bp_directory = (
            f'{Config.ROOT_DIRECTORY}/app/blueprints/{component_name}'
        )
        bp_test_directory = f'{bp_directory}/tests'
        bp_test_integration_directory = f'{bp_test_directory}/integration'
        directories = [
            bp_directory,
            bp_test_directory,
            bp_test_integration_directory,
        ]

        for directory in directories:
            os.mkdir(directory)

        return [component_name] + directories

    @staticmethod
    def __create_modules(
        component_name, bp_dirname, test_dirname, test_integration_dirname
    ):
        def build_comment(concept):
            return f'#  Insert your {concept} here.'

        service_file = (
            f'{Config.ROOT_DIRECTORY}/app/services/{component_name}_service.py'
        )

        component_files = {
            # blueprint
            f'{bp_dirname}/__init__.py': '',
            f'{bp_dirname}/blueprint.py': build_comment('endpoints'),
            f'{bp_dirname}/manager.py': build_comment('database queries'),
            f'{bp_dirname}/models.py': build_comment('models'),
            f'{bp_dirname}/serializers.py': build_comment('serializers'),
            f'{bp_dirname}/swagger.py': build_comment('swagger models'),
            # tests
            f'{test_dirname}/__init__.py': '',
            f'{test_integration_dirname}/__init__.py': '',
            f'{test_dirname}/factory.py': build_comment('factories'),
            f'{test_dirname}/seeder.py': build_comment('seeder'),
            # services
            service_file: build_comment('service'),
        }

        for file, file_content in component_files.items():
            with open(file, 'w') as fd:
                fd.write(file_content)

    def run_command(self, component_name):
        self.__create_modules(*self.__create_packages(component_name))
