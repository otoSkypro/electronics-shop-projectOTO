import pytest
from src.phone import Phone
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def item1():
    item = Item("Смартфон", 10000, 20)
    return item


@pytest.fixture
def phone1():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1


@pytest.fixture
def kb1():
    kb1 = Keyboard('Dark Project KD87A', 9600, 5)
    return kb1