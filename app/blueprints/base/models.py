import logging
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP

logger = logging.getLogger(__name__)


class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(
        TIMESTAMP, default=datetime.utcnow, server_default=None, nullable=False
    )
    updated_at = Column(
        TIMESTAMP,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
    deleted_at = Column(TIMESTAMP, server_default=None, nullable=True)
