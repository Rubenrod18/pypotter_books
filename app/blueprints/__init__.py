import os

from app.utils import get_attr_from_module


def get_blueprints() -> list:
    """Get Blueprints via dynamic way."""
    def get_bp_modules() -> list:
        """Get Blueprints modules."""
        abs_path = os.path.abspath(__file__)
        path = os.path.dirname(abs_path)
        dirs = os.listdir(path)
        dirs.remove(os.path.basename(__file__))
        dirs.remove('__pycache__')

        bp_modules = []
        for item in dirs:
            abs_path_module = '{}.{}.blueprint'.format(__name__, item)
            bp_modules.append(abs_path_module)

        return bp_modules

    def get_bp_instances(modules: list) -> list:
        """Get Blueprints instances."""
        blueprints = []

        for item in modules:
            bp = get_attr_from_module(item, 'blueprint')
            blueprints.append(bp)

        return blueprints

    bp_modules = get_bp_modules()
    return get_bp_instances(bp_modules)


BLUEPRINTS = get_blueprints()
