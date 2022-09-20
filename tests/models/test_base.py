from typing import Iterable

import pytest
from pytest_mock import MockerFixture
from pyutils.lister import is_matched
from sqlalchemy import inspect
from sqlalchemy.engine.base import Engine

from kindledb_common.database.base import Base
from kindledb_common.database.session import create_scoped_session
from tests.test_utils.test_enver import EnvForTest

env_param: dict = {
    "ENV_TEST1": "aiueo123",
    "ENV_TEST2": "@@test",
    "RDBMS": "sqlite",
    "DB_DRIVER": "pysqlite",
    "DB_DATABASE": ":memory:",
}


@pytest.fixture
def engine(mocker: MockerFixture) -> Iterable[Engine]:
    mocker.patch("kindledb_common.utils.enver.dotenv_values", return_value=env_param)
    sessionmaker, engine = create_scoped_session(
        EnvForTest(),
        shouldInitialize=True,
    )
    yield engine


def test_models_base(engine: Engine):
    assert is_matched(
        inspect(engine).get_table_names(), list(Base.metadata.tables.keys())
    )
