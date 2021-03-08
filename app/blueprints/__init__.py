import os

from app.utils import get_attr_from_module


def get_bp_paths():
    """Get Blueprints paths."""
    abs_path = os.path.abspath(__file__)
    path = os.path.dirname(abs_path)
    dirs = os.listdir(path)
    dirs.remove(os.path.basename(__file__))
    dirs.remove('__pycache__')
    return [f'{__name__}.{item}' for item in dirs]


def _get_bp_modules() -> list:
    """Get Blueprints modules."""
    bp_modules = []
    for item in get_bp_paths():
        abs_path_module = f'{item}.blueprint'
        bp_modules.append(abs_path_module)

    return bp_modules


def _get_bp_instances(modules: list) -> list:
    """Get Blueprints instances."""
    blueprints = []

    for item in modules:
        bp = get_attr_from_module(item, 'blueprint')
        blueprints.append(bp)

    return blueprints


def _get_blueprints() -> list:
    """Get Blueprints via dynamic way."""
    bp_modules = _get_bp_modules()
    return _get_bp_instances(bp_modules)


BLUEPRINTS = _get_blueprints()
