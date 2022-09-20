from pyutils.datetimer import datetime

from kindledb_common.models.historical.rate import Rate

data = [
    Rate(
        asin="test_asin1",
        average_rate=3.1,
        rate_count=10,
        created=datetime("2020-01-01T00:00:00"),
    ),
    Rate(
        asin="test_asin1",
        average_rate=3.1,
        rate_count=10,
        created=datetime("2020-01-02T00:00:00"),
    ),
    Rate(
        asin="test_asin1",
        average_rate=3.1,
        rate_count=10,
        created=datetime("2020-01-03T00:00:00"),
    ),
    Rate(
        asin="test_asin2",
        average_rate=4.1,
        rate_count=100,
        created=datetime("2020-01-01T00:00:00"),
    ),
]
