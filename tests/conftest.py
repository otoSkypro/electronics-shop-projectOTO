import pytest

from src.item import Item


@pytest.fixture
def item1():
    item = Item("Смартфон", 10000, 20)
    return item