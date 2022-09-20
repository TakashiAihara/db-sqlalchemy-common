from datetime import datetime

from inflection import underscore
from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func


class CommonCore(object):
    @declared_attr
    def __tablename__(cls):
        return underscore(cls.__name__)  # type: ignore

    created = Column(DateTime(timezone=True), server_default=func.now())

    __mapper_args__ = {"always_refresh": True}


class CommonCoreSchema(BaseModel):
    created: datetime
