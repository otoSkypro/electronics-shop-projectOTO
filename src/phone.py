# from src.item import Item
#
#
# class Phone(Item):
#     # phone1: None
#
#     #
#     # def __init__(self,phone1.number_of_sim: int):
#     #     self.sim_quantity = sim_quantity
#     #     super().__init__(?????)
#     #
#     #
#     # def __add__(self, other):
#     #     return self.quantity + other.quantity
#
#     def __init__(self, title: str, prise: float, quantity: int, number_of_sim: int):
#         # self.title = title
#         # self.prise = prise
#         # self.quantity = quantity
#         self.number_of_sim = number_of_sim
#         super().__init__(title, prise, quantity, number_of_sim)
#
#     def __add__(self, other):
#         if isinstance(other, (Phone, Item)):
#             return self.quantity + other.quantity
#         raise TypeError(f"Cannot add {type(other)} to {type(self)}")
#             # return Phone(self.title, self.prise + other.prise, self.quantity + other.quantity, self.number_of_sim)
#
#     def __repr__(self, ) -> str:
#         return (f"{self.__class__.__name__}(title='{self.title}', prise={self.prise}, quantity={self.quantity}, "
#                 f"number_of_sim={self.number_of_sim})")
#
#     # def __repr__(self, ) -> str:
#     #     return (f"{self.__class__.__name__}(name='{self.name}', price={self.price}, quantity={self.quantity}, "
#     #             f"number_of_sim={self.number_of_sim})")
from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
        raise TypeError("Unsupported operand type(s) for +: {} and {}".format(type(self), type(other)))

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"