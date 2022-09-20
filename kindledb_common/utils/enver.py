from copy import deepcopy
from os import environ, getenv

from dotenv import dotenv_values
from pyutils.pather import get_git_root

from constants import (
    DEFAULT_ENV_FILE_SUFFIX,
    ENV_FILE_BASE_PATH,
    ENV_FILE_PREFIX,
    ENVIRONMENT_CONTEXT,
)


class Env:
    def __init__(
        self,
        env: str = DEFAULT_ENV_FILE_SUFFIX,
        env_file_path=ENV_FILE_BASE_PATH,
    ):

        self.env = getenv(ENVIRONMENT_CONTEXT, env)

        self.os_env = deepcopy(dict(environ))

        self.file_env = dotenv_values(
            dotenv_path=f"{get_git_root()}{env_file_path}{ENV_FILE_PREFIX}{env}",
            verbose=True,
        )
        self.all_env = deepcopy(self.file_env)

        self.all_env.update(deepcopy(self.os_env))

    def __repr__(self):
        return ",".join(self.generate_dict())

    def __str__(self):
        return ",".join(self.generate_dict())

    def generate_dict(self):
        for k, v in self.all_env.items():
            yield f"{k}: {v}"

    def get(self, key) -> str:
        return self.all_env.get(key) or ""

    def get_from_all(self) -> dict:
        return self.all_env

    def get_from_os(self) -> dict:
        return self.os_env

    def get_from_file(self) -> dict:
        return self.file_env
