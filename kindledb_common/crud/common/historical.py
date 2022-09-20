from copy import deepcopy

from sqlalchemy.orm import Session

from kindledb_common.models.common.common_historical import CommonHistorical

remove_keys = [
    "id",
    "created",
    "_sa_instance_state",
]


# TODO: support mixin type hints
def get_one(session: Session, clz, asin: str):
    return session.query(clz).filter(clz.asin == asin).first()


def exists(session: Session, clz, asin: str) -> bool:
    return session.query(session.query(clz).filter(clz.asin == asin).exists()).scalar()


def get_all(
    session: Session,
    clz,
    skip: int = 0,
    limit: int = 100,
):
    return session.query(clz).offset(skip).limit(limit).all()


def get_latest(session: Session, clz):
    return session.query(clz).order_by(clz.created.desc()).first()


def get_dict_data(clz):
    target = deepcopy(clz.__dict__)
    remove_unnecessary_keys(target)
    return target


def remove_unnecessary_keys(target: dict):
    for key in remove_keys:
        target.pop(key, None)


def is_latest_one_matched(session: Session, clz, target) -> bool:
    latest = get_latest(session, clz)
    if latest is None:
        return False
    return get_dict_data(latest) == get_dict_data(target)


def create_one(session: Session, clz) -> CommonHistorical:
    session.add(clz)
    session.commit()
    session.refresh(clz)
    return clz
