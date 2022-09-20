from pyutils.globber import glob
from pyutils.moduler import import_module
from sqlalchemy.orm import Session

from constants import SEEDS_PATH
from kindledb_common.database.base import drop_all_table


def get_seed_files(seeds_path: str) -> list[str]:
    return glob(f"{seeds_path}**/*.py", recursive=True, exclude_init=True, sort=True)


def pour_in(session: Session, seeds_path: str = SEEDS_PATH) -> None:
    for seed_file in get_seed_files(seeds_path):
        data: list = import_module(seed_file).data
        session.add_all(data)
        session.commit()


def pour_out(session: Session) -> None:
    drop_all_table(session.bind)

    session.close()
