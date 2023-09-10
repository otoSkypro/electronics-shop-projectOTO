import csv
import os


class Item:
    """
        Класс для представления товара в магазине.
        @@ -13,18 +16,44 @@ def __init__(self, name: str, price: float, quantity: int) -> None:
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
    pay_rate = 0.85
    all_instances = []

    def __init__(self, name, price, quantity):
        self.__name = None
        self.name = name
        self.price = price
        self.quantity = self.string_to_number(quantity)
        self.all_instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))


    @classmethod
    def instantiate_from_csv(cls):
        current_dir = os.path.dirname(__file__)
        items_csv_path = os.path.join(current_dir, 'items.csv')

        with open(items_csv_path, newline='', encoding='UTF-8') as file:
            data = csv.DictReader(file)
            for row in data:
                cls(row['name'], row['price'], row['quantity'])







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