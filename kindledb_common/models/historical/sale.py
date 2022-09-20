from sqlalchemy import Boolean, Column

from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonHistorical, CommonHistoricalSchema


class Sale(CommonHistorical, Base):
    sale = Column(
        Boolean,
        index=False,
        nullable=True,
    )


class SaleBaseSchema(CommonHistoricalSchema):
    pass


class SaleCreateSchema(SaleBaseSchema):
    sale: bool


class SaleSchema(SaleBaseSchema):
    class Config:
        orm_mode = True
