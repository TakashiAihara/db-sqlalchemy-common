from typing import List

from datetime import datetime

from pydantic import BaseModel, Field
from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.orm import relationship

from constants import ASIN_LENGTH
from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonCore
from kindledb_common.models.historical import (
    PointSchema,
    PriceSchema,
    RateSchema,
    SaleSchema,
    UnlimitedSchema,
)


class Kindle(CommonCore, Base):
    prices = relationship("Price", backref="kindle", cascade="all, delete-orphan")
    points = relationship("Point", backref="kindle", cascade="all, delete-orphan")
    rates = relationship("Rate", backref="kindle", cascade="all, delete-orphan")
    unlimiteds = relationship(
        "Unlimited", backref="kindle", cascade="all, delete-orphan"
    )

    asin = Column(
        String(ASIN_LENGTH),
        index=False,
        nullable=False,
        primary_key=True,
    )
    title = Column(
        Text,
        index=True,
        nullable=False,
    )
    series = Column(
        Text,
        index=True,
        nullable=True,
    )
    image_url = Column(
        Text,
        index=False,
        nullable=True,
    )
    published = Column(
        Date,
        index=False,
        nullable=True,
    )
    context_date = Column(
        Date,
        index=False,
        nullable=True,
    )
    page_size = Column(
        Integer,
        index=False,
        nullable=True,
    )


class KindleBaseSchema(BaseModel):
    prices: List[PriceSchema] = []
    points: List[PointSchema] = []
    rates: List[RateSchema] = []
    unlimiteds: List[UnlimitedSchema] = []
    sale: List[SaleSchema] = []

    asin: str = Field(..., max_length=ASIN_LENGTH)
    title: str
    series: str | None = None
    image_url: str | None = None
    published: datetime | None = None
    page_size: int | None = None


class KindleCreateSchema(KindleBaseSchema):
    pass


class KindleSchema(KindleBaseSchema):
    class Config:
        orm_mode = True
