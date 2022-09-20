import fire

from constants import DEFAULT_ENV_FILE_SUFFIX
from kindledb_common.database.session import create_scoped_session
from kindledb_common.utils.enver import Env
from kindledb_common.utils.seeder import pour_in, pour_out


def up(env: str = DEFAULT_ENV_FILE_SUFFIX, data: bool = False):
    env_instance = Env(env=env)
    sessionmaker, engine = create_scoped_session(
        env=env_instance, shouldInitialize=True
    )
    if data:
        pour_in(sessionmaker())


def down(env: str = DEFAULT_ENV_FILE_SUFFIX):
    sessionmaker, engine = create_scoped_session(
        env=Env(env=env), shouldInitialize=False
    )
    pour_out(sessionmaker())


if __name__ == "__main__":
    fire.Fire({"up": up, "down": down})
