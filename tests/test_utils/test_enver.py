from constants import ENV_FILE_BASE_PATH_TEST, ENV_FILE_SUFFIX_TEST
from kindledb_common.utils.enver import Env


class EnvForTest(Env):
    def __init__(
        self,
    ):
        super().__init__(
            env=ENV_FILE_SUFFIX_TEST,
            env_file_path=ENV_FILE_BASE_PATH_TEST,
        )
