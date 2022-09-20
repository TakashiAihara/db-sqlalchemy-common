from datetime import datetime

from inflection import underscore
from pydantic import BaseModel, Field
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func

from constants import ASIN_LENGTH


class CommonHistorical(object):
    @declared_attr
    def __tablename__(cls):
        return underscore(cls.__name__)  # type: ignore

    @declared_attr
    def asin(cls):
        return Column(String(ASIN_LENGTH), ForeignKey("kindle.asin"))

    created = Column(DateTime(timezone=True), server_default=func.now())
    id = Column(Integer, autoincrement=True, primary_key=True)

    __mapper_args__ = {"always_refresh": True}


class CommonHistoricalSchema(BaseModel):
    id: int
    created: datetime
    asin: str = Field(..., max_length=ASIN_LENGTH)
