from sqlalchemy.orm import Session

from kindledb_common.crud.common import historical
from kindledb_common.models.common.common_historical import CommonHistorical
from kindledb_common.models.historical.price import Price


def get_one(session: Session, asin: str):
    return historical.get_one(session, Price, asin)


def exists(session: Session, asin: str) -> bool:
    return historical.exists(session, Price, asin)


def get_all(session: Session, skip: int = 0, limit: int = 100):
    return historical.get_all(session, Price, skip, limit)


def get_latest_one(session: Session):
    return historical.get_latest(session, Price)


def is_latest_one_matched(session: Session, target):
    return historical.is_latest_one_matched(session, Price, target)


def create_one(session: Session, price: Price) -> CommonHistorical:
    return historical.create_one(session, price)
