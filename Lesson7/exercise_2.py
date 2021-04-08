# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Для получения того же результата, можно было обойтись  без наследования АВС и без .setter, но я старался использовать
# всё, что было показано в лекции. Возможно, я не правильно понял задание.
from abc import ABC, abstractmethod


class Clothes(ABC):
    material_consumed = 0

    @abstractmethod
    def material_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v
        self.material_consumption = None

    @property
    def material_consumption(self):
        return f'Расходовано ткани для пальто: {self.__material_consumption}'

    @material_consumption.setter
    def material_consumption(self, material_consumption):
        self.__material_consumption = self.v / 6.5 + 0.5
        Clothes.material_consumed += self.__material_consumption


class Suit(Clothes):
    def __init__(self, h):
        self.h = h
        self.material_consumption = None

    @property
    def material_consumption(self):
        return f'Расходовано ткани для костюма: {self.__material_consumption}'

    @material_consumption.setter
    def material_consumption(self, material_consumption):
        self.__material_consumption = 2 * self.h + 0.3
        Clothes.material_consumed += self.__material_consumption


coat = Coat(52)
suit = Suit(1.8)

print(coat.material_consumption)
print(suit.material_consumption)
print(Clothes.material_consumed)



