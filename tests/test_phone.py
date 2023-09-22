from src import phone
from src.phone import Phone
from src.item import Item


def test_phone_inheritance():
    phone = Phone("Смартфон", 10000, 20, 2)
    assert isinstance(phone, Item)
    assert hasattr(phone, 'name')
    assert hasattr(phone, 'price')
    assert hasattr(phone, 'quantity')
    assert hasattr(phone, 'number_of_sim')

def test_number_of_sim():
    assert isinstance(test_number_of_sim(), Phone)

def test_raises_exception():
    assert isinstance(test_raises_exception)




def test_is_phone_inheritance():
    assert isinstance(isinstance(phone))

# def test_add_phone_and_non_item_or_phone():
#
#     phone = Phone("Смартфон", 10000, 20, 2)
#     non_item = "This is not an Item or Phone"
#     try:
#         phone + non_item
#     except TypeError as e:
#         assert str(e) == "Unsupported operand type(s) for +: <class 'src.phone.Phone'> and <class 'str'>"
