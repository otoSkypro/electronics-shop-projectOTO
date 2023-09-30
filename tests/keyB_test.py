import pytest


def test_kb_init(kb1):
    assert isinstance(kb1.name, str)
    assert isinstance(kb1.price, int)
    assert isinstance(kb1.quantity, int)
    with pytest.raises(AttributeError):
        kb1.language = "CH"


def test_lang(kb1):
    assert kb1.language == "EN"


def test_change_lang(kb1):
    kb1.change_lang()
    assert kb1.language == "RU"
    kb1.change_lang()
    assert kb1.language == "EN"