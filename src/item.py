import csv
import os.path
from src.instantiateCSVError import InstantiateCSVError

filename = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.join(filename)


    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        pass
        super().__init__()
        Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = int(quantity)

    @property
    def short_name(self):
        return self.name[:10]

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        print("Эти объекты нельзя сложить")

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        if not os.path.exists(cls.CSV_PATH):
            raise FileNotFoundError(f"Отсутствует файл {filename}")
        try:
            with open(cls.CSV_PATH, newline='', encoding='cp1251') as f:
                data = csv.DictReader(f)
                for row in data:
                    price_int = cls.string_to_number(row['price'])
                    quantity_int = cls.string_to_number(row['quantity'])
                    cls(row['name'], price_int, quantity_int)
        except(KeyError, TypeError):
            raise InstantiateCSVError(f'Файл {filename} поврежден')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate