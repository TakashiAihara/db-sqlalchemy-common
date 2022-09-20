from pyutils.datetimer import date

from kindledb_common.models.historical.price import Price

data = [
    Price(
        asin="test_asin1",
        price=100,
    ),
    Price(
        asin="test_asin1",
        price=200,
    ),
    Price(
        asin="test_asin1",
        price=300,
    ),
    Price(
        asin="test_asin2",
        price=1000,
    ),
]
