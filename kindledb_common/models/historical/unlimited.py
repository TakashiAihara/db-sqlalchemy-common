from sqlalchemy import Boolean, Column

from kindledb_common.database.base import Base
from kindledb_common.models.common import CommonHistorical, CommonHistoricalSchema


class Unlimited(CommonHistorical, Base):
    unlimited = Column(
        Boolean,
        index=False,
        nullable=False,
    )


class UnlimitedBaseSchema(CommonHistoricalSchema):
    pass


class UnlimitedCreateSchema(UnlimitedBaseSchema):
    unlimited: bool


class UnlimitedSchema(UnlimitedBaseSchema):
    class Config:
        orm_mode = True
