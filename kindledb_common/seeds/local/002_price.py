from pyutils.datetimer import datetime

from kindledb_common.models.historical.price import Price

data = [
    Price(
        asin="test_asin1",
        price=30,
        created=datetime("2020-01-01T00:00:00"),
    ),
    Price(
        asin="test_asin1",
        price=40,
        created=datetime("2020-01-02T00:00:00"),
    ),
    Price(
        asin="test_asin1",
        price=50,
        created=datetime("2020-01-03T00:00:00"),
    ),
    Price(
        asin="test_asin2",
        price=50,
        created=datetime("2020-01-01T00:00:00"),
    ),
]
