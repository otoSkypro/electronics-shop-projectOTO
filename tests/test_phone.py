def test_phone_init(phone1):
    assert isinstance(phone1.name, str)
    assert isinstance(phone1.price, int)
    assert isinstance(phone1.quantity, int)
    assert isinstance(phone1.number_of_sim, int)


def test_add(item1, phone1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10