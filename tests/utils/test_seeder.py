from typing import Iterable

import pytest
from pytest_mock import MockerFixture
from pyutils.moduler import import_module
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from kindledb_common.database.base import import_modules
from kindledb_common.database.session import create_scoped_session
from kindledb_common.utils.enver import Env
from kindledb_common.utils.seeder import pour_in, pour_out
from tests.test_utils.test_enver import EnvForTest

env_param: dict = {
    "ENV_TEST1": "aiueo123",
    "ENV_TEST2": "@@test",
    "RDBMS": "sqlite",
    "DB_DRIVER": "pysqlite",
    "DB_DATABASE": ":memory:",
}


@pytest.fixture
def test_data(mocker: MockerFixture) -> Iterable[tuple[Session, Engine, Env]]:
    mocker.patch("kindledb_common.utils.enver.dotenv_values", return_value=env_param)
    env = EnvForTest()
    sessionmaker, engine = create_scoped_session(
        env,
        shouldInitialize=True,
    )
    yield (sessionmaker(), engine, env)


def test_pour_in(test_data: tuple[Session, Engine, Env]):
    pour_in(test_data[0])


def test_pour_out(test_data: tuple[Session, Engine, Env]):
    pour_out(test_data[0])
