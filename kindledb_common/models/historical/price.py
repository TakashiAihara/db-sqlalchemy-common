from sqlalchemy import Column, Integer

from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonHistorical, CommonHistoricalSchema


class Price(CommonHistorical, Base):
    price = Column(
        Integer,
        index=False,
        nullable=False,
    )


class PriceBaseSchema(CommonHistoricalSchema):
    pass


class PriceCreateSchema(PriceBaseSchema):
    price: int


class PriceSchema(PriceBaseSchema):
    class Config:
        orm_mode = True
