# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, kg_per_meter, thickness):
        print(self._length * self._width * kg_per_meter * thickness / 1000, "т")


my_road = Road(5000, 20)
my_road.calculate_weight(25, 5)


