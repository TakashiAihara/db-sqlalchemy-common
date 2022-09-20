from typing import Iterable

import pytest
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from constants import TEST_SEEDS_PATH
from kindledb_common.crud.price import create_one, get_one, is_latest_one_matched
from kindledb_common.database.base import Base
from kindledb_common.database.session import create_scoped_session
from kindledb_common.models.core.kindle import Kindle
from kindledb_common.models.historical.price import Price
from kindledb_common.utils.seeder import pour_in
from tests.test_utils.test_enver import EnvForTest


@pytest.fixture(scope="session", autouse=True)
def setup():
    # mocker.patch("kindledb_common.utils.enver.dotenv_values", return_value=env_param)
    scoped_session, engine = create_scoped_session(
        EnvForTest(),
        shouldInitialize=True,
    )
    session: Session = scoped_session()
    Base.metadata.create_all(bind=engine)
    pour_in(session, seeds_path=TEST_SEEDS_PATH)
    session.flush()
    session.close()
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def session():
    scoped_session, engine = create_scoped_session(
        EnvForTest(),
        shouldInitialize=True,
    )
    yield scoped_session()


def test_get_one(session):
    create_one(session, Kindle(asin="1", title="test"))  # TODO: to fixture
    create_one(session, Price(asin="1", price=1))
    session.commit()
    result = get_one(session, asin="1")
    assert type(result) == Price


def test_is_latest_one_match(session):
    create_one(session, Kindle(asin="2", title="test"))
    create_one(session, Price(asin="2", price=100))
    session.commit()

    target = Price(asin="2", price=100)
    assert is_latest_one_matched(session, target) == True

    target = Price(asin="2", price=200)
    assert is_latest_one_matched(session, target) == False
