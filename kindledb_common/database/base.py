from types import ModuleType

from collections.abc import Iterable

from pyutils.globber import glob
from pyutils.moduler import import_modules as im
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base

from constants import MODELS_PATH

Base = declarative_base()


def import_modules() -> Iterable[ModuleType]:
    return im(glob(f"{MODELS_PATH}**/*.py", recursive=True, exclude_init=True))


def create_all_table(engine: Engine) -> None:
    Base.metadata.create_all(bind=engine)


def drop_all_table(engine: Engine) -> None:
    Base.metadata.drop_all(bind=engine)


import_modules()
