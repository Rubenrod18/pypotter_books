import logging
import typing as t

from flask import request

from app.extensions import cache


logger = logging.getLogger(__name__)


class CacheWrapper:
    @classmethod
    def make_cache_key(cls) -> str:
        """Build a custom key_prefix.

        Returns
        -------
        str
            For example::

                get/api/roles/1
                post/api/roles

        """
        return f'{request.method}{request.path}'.lower()

    @classmethod
    def delete(cls, *args) -> t.List[bool]:
        """Remove a list of cache names."""
        deleted_caches = []

        for cache_name in args:
            deleted_caches.append(cache.delete(cache_name))

        if sum(deleted_caches) != sum(args):
            logger.error(f'The next cache names {args} haven\'t been deleted.')

        return deleted_caches
