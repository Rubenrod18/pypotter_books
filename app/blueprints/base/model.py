import logging
from datetime import datetime

from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.util.compat import contextmanager

from app.extensions import db

logger = logging.getLogger(__name__)


class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow,
                        server_default=None, nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(TIMESTAMP, server_default=None, nullable=True)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations.

    References
    ----------
    When do I construct a Session, when do I commit it, and when do I close it?
    https://docs.sqlalchemy.org/en/13/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it

    """
    session = db.Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        logger.debug(e)
        session.rollback()
        raise
    finally:
        session.close()
