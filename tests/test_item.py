def test_item_init(item1):
    isinstance(item1.name,str)
    isinstance(item1.price,float)
    isinstance(item1.quantity,int)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_apply_discount(item1):
    item1.pay_rate = 1.5
    item1.apply_discount()
    assert item1.price == 15000

def test_item(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
