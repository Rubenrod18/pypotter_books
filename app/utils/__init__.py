"""Collection of functions and classes which make common patterns
shorter and easier."""
import importlib


def get_attr_from_module(module: str, attr: str) -> any:
    """Get attribute from a module.

    Parameters
    ----------
    module : str
        Module absolute path.
    attr : str
        Module's attribute. It could be any kind of variable belongs to module.

    Examples
    --------

    >>> from app.utils import get_attr_from_module
    >>> module_path = 'app.blueprints.base'
    >>> module_attr = 'blueprint'
    >>> get_attr_from_module(module_path, module_attr)
    <flask.blueprints.Blueprint object at ...>

    Raises
    ------
    ImportError
        Module doesn't exist.
    AttributeError
        Attribute doesn't exist in module.

    """
    m = importlib.import_module(module)
    return getattr(m, attr)


def exists_attr_in_module(module: str, attr: str) -> bool:
    """Check if an attribute exists in a module.

    Parameters
    ----------
    module : str
        Module absolute path.
    attr : str
        Module's attribute. It could be any kind of variable belongs to module.

    Returns
    -------
    bool
        True if exists, otherwise False.

    Example
    --------
    >>> from app.utils import exists_attr_in_module
    >>> module_path = 'app.blueprints.base'
    >>> module_attr = 'blueprint'
    >>> exists_attr_in_module(module_path, module_attr)
    True

    """
    exists = False
    try:
        attr = get_attr_from_module(module, attr)
        if attr:
            exists = True
    except ImportError:
        pass
    except AttributeError:
        pass

    return exists


def ignore_keys(data: dict, exclude: list) -> dict:
    return dict({item: data[item] for item in data if item not in exclude})


def filter_by_keys(data: dict, keys: list) -> dict:
    return {key: value for key, value in data.items() if key in keys}
