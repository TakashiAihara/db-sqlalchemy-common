from setuptools import find_packages, setup

setup(
    name="kindledb-common",
    version="0.1.1",
    packages=find_packages(),
    entry_points={"scrapy": ["settings = kindledb_common.settings"]},
)
