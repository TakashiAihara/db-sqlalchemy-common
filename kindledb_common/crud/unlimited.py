from sqlalchemy.orm import Session

from kindledb_common.crud.common import historical
from kindledb_common.models.common.common_historical import CommonHistorical
from kindledb_common.models.historical.unlimited import Unlimited


def get_one(session: Session, asin: str):
    return historical.get_one(session, Unlimited, asin)


def exists(session: Session, asin: str) -> bool:
    return historical.exists(session, Unlimited, asin)


def get_all(session: Session, skip: int = 0, limit: int = 100):
    return historical.get_all(session, Unlimited, skip, limit)


def get_latest_one(session: Session):
    return historical.get_latest(session, Unlimited)


def is_latest_one_matched(session: Session, target):
    return historical.is_latest_one_matched(session, Unlimited, target)


def create_one(session: Session, unlimited: Unlimited) -> CommonHistorical:
    return historical.create_one(session, unlimited)
