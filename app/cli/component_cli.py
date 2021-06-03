import os
from abc import ABC
from distutils.dir_util import copy_tree

from app.cli._base_cli import _BaseCli
from config import Config


class ComponentCli(_BaseCli, ABC):
    @staticmethod
    def __create_package(component_name: str):
        serialized_name = (
            component_name.replace('-', ' ').lower().replace(' ', '_')
        )
        bp_package = (
            f'{Config.ROOT_DIRECTORY}/app/blueprints/{serialized_name}'
        )
        os.mkdir(bp_package)
        return component_name, bp_package

    @staticmethod
    def __create_modules(component_name: str, bp_package: str):
        component_structure_template = (
            f'{Config.ROOT_DIRECTORY}/app/cli/component_structure_template'
        )

        pascal_case_component_name = (
            component_name.replace('_', ' ')
            .replace('-', ' ')
            .title()
            .replace(' ', '')
        )
        snake_case_component_name = (
            component_name.replace('-', ' ').lower().replace(' ', '_')
        )

        copy_tree(component_structure_template, bp_package)

        for root, dirs, files in os.walk(bp_package, topdown=True):
            for name in files:
                src = os.path.join(root, name)

                with open(src, 'r') as fd:
                    filedata = fd.read()

                filedata = filedata.replace(
                    'ComponentPascalCase', pascal_case_component_name
                ).replace('component_snake_case', snake_case_component_name)

                with open(src, 'w') as fd:
                    fd.write(filedata)

                pre, ext = os.path.splitext(src)
                os.rename(src, pre + '.py')

    def run_command(self, component_name):
        self.__create_modules(*self.__create_package(component_name))
