"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_phone_inheritance():
    phone = Phone("Смартфон", 10000, 20, 2)
    assert isinstance(phone, Item)
    assert hasattr(phone, 'name')
    assert hasattr(phone, 'price')
    assert hasattr(phone, 'quantity')
    assert hasattr(phone, 'number_of_sim')

def test_repr(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_str(item1):
    assert str(item1) == 'Смартфон'

def test_item_init(item1):
        assert item1.name == "Смартфон"
        assert item1.price == 10000
        assert item1.quantity == 20
        assert item1.total_price == 200000





def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_item_apply_discount(item1):
    item1.__class__.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 5000

def test_item_long_name(item1):
    item1.name = "ОченьДлинноеНаименование"
    assert item1.name == "ОченьДлинн"

def test_item_initate_from_file():
    Item.all_instances = []
    Item.instantiate_from_csv()
    assert len(Item.all_instances) == 5

def test_add(item):
    item.add()
    assert len(Item.all_instances) == 6


