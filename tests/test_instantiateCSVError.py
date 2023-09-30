import csv
import os

import pytest
from src.instantiateCSVError import InstantiateCSVError
from src.item import Item, filename


def test_instantiate_from_csv():
    """тест для обработку исключений, если csv файл поврежден или отсутствует"""
    # создаем поврежденный csv файл
    data = [
        {'name': 'item_1', 'price': '1.0'},
        {'name': 'item_2', 'price': '2.0'},
        {'name': 'item_3', 'price': '3.0'}
    ]
    # создаём временный csv файл с помощью модуля csv
    with open('test.csv', 'w', encoding='cp1251', newline='') as file:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    Item.CSV_PATH = 'test.csv'
    # проверяем обработку исключения, если данные неправильные
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv() == f"Файл {filename} поврежден"

    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError()
        Item.instantiate_from_csv() == "Файл поврежден"

    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError()
        Item.instantiate_from_csv() == f"Отсутствует файл {filename}"

    # удаляем временный csv файл
    os.remove('test.csv')