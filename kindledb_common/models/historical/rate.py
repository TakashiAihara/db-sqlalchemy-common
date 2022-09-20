from sqlalchemy import Column, Float, Integer

from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonHistorical, CommonHistoricalSchema


class Rate(CommonHistorical, Base):
    average_rate = Column(
        Float,
        index=False,
        nullable=False,
    )
    rate_count = Column(
        Integer,
        index=False,
        nullable=False,
    )


class RateBaseSchema(CommonHistoricalSchema):
    pass


class RateCreateSchema(RateBaseSchema):
    average_rate: float
    rate_count: int


class RateSchema(RateBaseSchema):
    class Config:
        orm_mode = True
