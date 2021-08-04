import os

from app.helpers.module_helper import ModuleHelper


def _get_blueprint_packages():
    """Get package names from `app.blueprints` package.

    Returns
    -------
    list
        Contains package names.

    Example
    -------
    ['auth', 'base', 'role', 'user']

    """
    abs_path = os.path.abspath(__file__)
    path = os.path.dirname(abs_path)
    dirs = os.listdir(path)
    dirs.remove(os.path.basename(__file__))
    dirs.remove('__pycache__')
    dirs.sort()
    return dirs


def _get_bp_instances(modules: list) -> list:
    """Get `flask.blueprints.Blueprint` instances from `app.blueprints` package.

    Returns
    -------
    list
        Contains `flask.blueprints.Blueprint` modules.

    Example
    -------
    [<flask.blueprints.Blueprint object at 0x11042cd00>,
    <flask.blueprints.Blueprint object at 0x110a56bb0>,
    <flask.blueprints.Blueprint object at 0x110b77610>,
    <flask.blueprints.Blueprint object at 0x11043f8e0>]

    """
    bp_instances = []

    for module in modules:
        if ModuleHelper.exists_attr_in_module(module, 'blueprint'):
            bp_instance = ModuleHelper.get_attr_from_module(
                module, 'blueprint'
            )
            bp_instances.append(bp_instance)

    return bp_instances


def _get_blueprints() -> list:
    """Get `flask.blueprints.Blueprint` via dynamic way from `app.blueprints`
    package.

    Example
    -------
    [<flask.blueprints.Blueprint object at 0x11042cd00>,
    <flask.blueprints.Blueprint object at 0x110a56bb0>,
    <flask.blueprints.Blueprint object at 0x110b77610>,
    <flask.blueprints.Blueprint object at 0x11043f8e0>]
    """
    bp_modules = [f'{item}.blueprint' for item in get_blueprint_modules()]
    return _get_bp_instances(bp_modules)


def get_blueprint_modules():
    """Get modules from `app.blueprints` package.

    Returns
    -------
    list
        Contains modules.

    Example
    -------
    >>> from app.blueprints import get_blueprint_modules
    >>> get_blueprint_modules()
    ['app.blueprints.role', 'app.blueprints.auth', 'app.blueprints.user',
    'app.blueprints.base']

    """
    dirs = _get_blueprint_packages()
    return [f'{__name__}.{item}' for item in dirs]


BLUEPRINTS = _get_blueprints()
