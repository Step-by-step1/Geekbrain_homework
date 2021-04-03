# 3. Реализовать базовый класс Worker (работник)
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя работника: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учётом премии: {self._income['wage'] + self._income['bonus']}")


some_worker = Position("Иван", "Снытко", "Дворник", {"wage": 10000, "bonus": 500})
print(some_worker.name)
print(some_worker.surname)
print(some_worker.position)
some_worker.get_full_name()
some_worker.get_total_income()
