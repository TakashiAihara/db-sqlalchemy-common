from kindledb_common.models.core import Kindle
from kindledb_common.models.historical import Rate
from kindledb_common.utils.scrapyer import item_class_factory


class Example(object):
    bool143 = True
    bool2 = True
    blah = False
    foo = True
    foobar2000 = False


def test_item_class_factory():

    test_class = item_class_factory(Example)
    assert test_class.__name__ == "ExampleItem"

    test_instance = test_class(bool143="test_data")
    assert test_instance["bool143"] == "test_data"
