from typing import Iterable

import pytest
from pytest_mock import MockerFixture
from pyutils.datetimer import date
from sqlalchemy.orm import Session

from constants import TEST_SEEDS_PATH
from kindledb_common.crud.kindle import create_one, exists, get_all, get_one
from kindledb_common.database.base import Base
from kindledb_common.database.session import create_scoped_session
from kindledb_common.models.core.kindle import Kindle, KindleCreateSchema
from kindledb_common.utils.seeder import pour_in
from tests.test_utils.test_enver import EnvForTest

create_data = Kindle(
    asin="test_asin3",
    title="test_title3",
    image_url="localhost",
    published=date("2020-03-03"),
    page_size=30,
)

create_data2 = Kindle(
    asin="test_asin3",
    title="test_title3",
    image_url="localhost",
    published=date("2020-03-03"),
    page_size=30,
)

env_param: dict = {
    "ENV_TEST1": "aiueo123",
    "ENV_TEST2": "@@test",
    "RDBMS": "sqlite",
    "DB_DRIVER": "pysqlite",
    "DB_DATABASE": ":memory:",
}


@pytest.fixture
def session(mocker: MockerFixture) -> Iterable[Session]:
    mocker.patch("kindledb_common.utils.enver.dotenv_values", return_value=env_param)
    scoped_session, engine = create_scoped_session(
        EnvForTest(),
        shouldInitialize=True,
    )
    session: Session = scoped_session()
    Base.metadata.create_all(bind=engine)
    pour_in(session, seeds_path=TEST_SEEDS_PATH)
    yield session
    session.flush()
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_get_one(session: Session):
    result: Kindle | None = get_one(session, asin="test_asin1")
    assert type(result) is Kindle


# TODO: fix all test
def test_exists(session: Session):
    result: Kindle | None = get_one(session, asin="test_asin1")
    assert exists(session, asin="test_asin1") == True
    assert exists(session, asin="thisasinisnotexists") == False


# def test_get_all(session: Session):

#     result: list[Kindle] | None = get_all(session)
#     assert all(type(r) is Kindle for r in result)
#     assert len(result) >= 2


def test_create_one(session: Session):
    assert create_data == create_one(session, create_data)
    assert get_one(session, create_data.asin) == create_data  # type: ignore
