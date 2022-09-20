from sqlalchemy.orm import Session

from kindledb_common.crud.common import historical
from kindledb_common.models.common.common_historical import CommonHistorical
from kindledb_common.models.historical.sale import Sale


def get_one(session: Session, asin: str):
    return historical.get_one(session, Sale, asin)


def exists(session: Session, asin: str) -> bool:
    return historical.exists(session, Sale, asin)


def get_all(session: Session, skip: int = 0, limit: int = 100):
    return historical.get_all(session, Sale, skip, limit)


def get_latest_one(session: Session):
    return historical.get_latest(session, Sale)


def is_latest_one_matched(session: Session, target):
    return historical.is_latest_one_matched(session, Sale, target)


def create_one(session: Session, sale: Sale) -> CommonHistorical:
    return historical.create_one(session, sale)
