from pyutils.datetimer import date, datetime

from kindledb_common.models.core.kindle import Kindle

data = [
    Kindle(
        asin="test_asin1",
        title="test_title",
        image_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png",
        published=date("2020-01-01"),
        page_size=30,
        created=datetime("2020-01-01T00:00:00"),
    ),
    Kindle(
        asin="test_asin2",
        title="test_title",
        image_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_92x30dp.png",
        published=date("2020-01-01"),
        page_size=30,
        created=datetime("2020-01-01T00:00:00"),
    ),
]
