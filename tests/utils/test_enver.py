from typing import Iterable

from os import environ

import pytest
from pytest_mock.plugin import MockerFixture

from kindledb_common.utils.enver import Env
from tests.test_utils.test_enver import EnvForTest

test_cases: list[dict] = [
    {"ENV_TEST1": "aiueo123", "ENV_TEST2": "@@test"},
]

env_param: dict = {
    "ENV_TEST1": "aiueo123",
    "ENV_TEST2": "@@test",
    "RDBMS": "sqlite",
    "DB_DRIVER": "pysqlite",
    "DB_DATABASE": ":memory:",
}

value = "test"
key = "ENV_OS_TEST"
environ[key] = value


@pytest.fixture
def env(mocker: MockerFixture) -> Iterable[Env]:
    mocker.patch("kindledb_common.utils.enver.dotenv_values", return_value=env_param)
    env = EnvForTest()
    yield env


def test_enver_os(env: Env):
    assert env.get(key) == value


@pytest.mark.parametrize("test_case", test_cases)
def test_enver_file(test_case: dict, env: Env):
    for k, v in test_case.items():
        assert env.get(k) == v


# @pytest.mark.parametrize("test_case", test_cases)
# def test_enver_os_overwrite(test_case, env):
#     k, v = list(test_case.items())[0]
#     environ[k] = v + "_os"

#     assert env.get(k) == v + "_os"
