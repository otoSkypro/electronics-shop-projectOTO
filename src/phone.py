from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = self.check_value(number_of_sim)

    def check_value(self, value):
        if not isinstance(value, int):
            raise ValueError('Значение должно быть целым числом.')
        elif value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        return value

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        self._number_of_sim = self.check_value(value)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
