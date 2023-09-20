from src.phone import Phone
from src.item import Item


def test_phone_inheritance():

    phone = Phone("Смартфон", 10000, 20, 2)
    assert isinstance(phone, Item)
    assert hasattr(phone, 'name')
    assert hasattr(phone, 'price')
    assert hasattr(phone, 'quantity')
    assert hasattr(phone, 'number_of_sim')


def test_add_phone_and_item():

    phone = Phone("Смартфон", 10000, 20, 2)
    item = Item("Ноутбук", 20000, 5)
    result = phone + item
    assert result == 25


def test_add_phone_and_phone():

    phone1 = Phone("Смартфон 1", 10000, 10, 1)
    phone2 = Phone("Смартфон 2", 12000, 15, 2)
    result = phone1 + phone2
    assert result == 25


def test_add_phone_and_non_item_or_phone():

    phone = Phone("Смартфон", 10000, 20, 2)
    non_item = "This is not an Item or Phone"
    try:
        phone + non_item
    except TypeError as e:
        assert str(e) == "Unsupported operand type(s) for +: <class 'src.phone.Phone'> and <class 'str'>"