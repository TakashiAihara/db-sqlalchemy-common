from sqlalchemy.orm import Session

from kindledb_common.models.core.kindle import Kindle


def get_one(session: Session, asin: str):
    return session.query(Kindle).filter(Kindle.asin == asin).first()


def exists(session: Session, asin: str) -> bool:
    return session.query(session.query(Kindle).filter(Kindle.asin == asin).exists()).scalar()


def get_all(session: Session, skip: int = 0, limit: int = 100):
    return session.query(Kindle).offset(skip).limit(limit).all()


def create_one(session: Session, kindle: Kindle) -> Kindle:
    session.add(kindle)
    session.commit()
    session.refresh(kindle)
    return kindle
