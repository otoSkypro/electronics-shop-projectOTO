from src.item import Item


class KeyBoardMixin:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, KeyBoardMixin):
    """Класс для клавиатуры со сменой языка"""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        KeyBoardMixin.__init__(self)