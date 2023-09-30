import pytest

from src.phone import Phone


def test_phone_init(phone1):
    assert isinstance(phone1.name, str)
    assert isinstance(phone1.price, int)
    assert isinstance(phone1.quantity, int)
    assert isinstance(phone1.number_of_sim, int)


def test_add(item1, phone1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_set_sim_card(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, -1)