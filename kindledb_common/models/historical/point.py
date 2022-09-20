from sqlalchemy import Column, Integer

from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonHistorical, CommonHistoricalSchema


class Point(CommonHistorical, Base):
    point = Column(
        Integer,
        index=False,
        nullable=False,
    )


class PointBaseSchema(CommonHistoricalSchema):
    pass


class PointCreateSchema(PointBaseSchema):
    point: int


class PointSchema(PointBaseSchema):
    class Config:
        orm_mode = True
