from typing import Any, Type

from pyutils.metaer import class_attributes
from pyutils.singleton import Singleton
from scrapy import Field, Item
from scrapy.item import ItemMeta


def item_class_factory(clz: type[Any]) -> type[Item]:
    class ItemMetaWrap(ItemMeta):
        def __new__(mcs, class_name, bases, attrs):
            class_name = clz.__name__ + "Item"

            for class_attribute in class_attributes(clz):
                attrs[class_attribute] = Field()

            return super().__new__(mcs, class_name, bases, attrs)

    class CommonItem(Item, metaclass=ItemMetaWrap):
        pass

    return CommonItem
