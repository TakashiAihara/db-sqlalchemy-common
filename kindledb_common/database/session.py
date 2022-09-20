from sqlite3 import Connection as SQLite3Connection

from pyutils.databaser import make_url
from sqlalchemy import create_engine as ce
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import create_database
from sqlalchemy_utils.functions import database_exists

from kindledb_common.database.base import create_all_table
from kindledb_common.utils.enver import Env


def initialize_database(engine: Engine):
    if not database_exists(engine.url):
        create_database(engine.url)


def create_sessionmaker(
    env: Env, shouldInitialize: bool = False
) -> tuple[sessionmaker, Engine]:
    engine = create_engine(env)

    if shouldInitialize:
        initialize(engine)

    return (sessionmaker(autocommit=False, autoflush=False, bind=engine), engine)


def create_scoped_session(
    env: Env, shouldInitialize: bool = False
) -> tuple[scoped_session, Engine]:
    sessionmaker, engine = create_sessionmaker(env, shouldInitialize)
    return scoped_session(sessionmaker), engine


def initialize(engine: Engine):
    initialize_database(engine)
    create_all_table(engine)


def create_engine(env: Env) -> Engine:
    return ce(
        url=make_url(
            rdbms=env.get("RDBMS"),
            host=env.get("DB_HOST"),
            driver=env.get("DB_DRIVER"),
            port=env.get("DB_PORT"),
            database=env.get("DB_DATABASE"),
            user=env.get("DB_USER"),
            password=env.get("DB_PASSWORD"),
        ),
        echo=True,
    )


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()
