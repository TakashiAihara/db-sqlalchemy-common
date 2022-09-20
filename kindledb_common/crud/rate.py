from sqlalchemy.orm import Session

from kindledb_common.crud.common import historical
from kindledb_common.models.common.common_historical import CommonHistorical
from kindledb_common.models.historical.rate import Rate


def get_one(session: Session, asin: str):
    return historical.get_one(session, Rate, asin)


def exists(session: Session, asin: str) -> bool:
    return historical.exists(session, Rate, asin)


def get_all(session: Session, skip: int = 0, limit: int = 100):
    return historical.get_all(session, Rate, skip, limit)


def get_latest_one(session: Session):
    return historical.get_latest(session, Rate)


def is_latest_one_matched(session: Session, target):
    return historical.is_latest_one_matched(session, Rate, target)


def create_one(session: Session, rate: Rate) -> CommonHistorical:
    return historical.create_one(session, rate)
