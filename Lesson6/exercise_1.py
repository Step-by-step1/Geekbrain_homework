# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Скорее всего я накодил совсем не то, что нужно. Честно говоря, задание лучше сформулировать поконкретней.
import time
from itertools import cycle


class TrafficLight:
    __color = zip(["красный", "жёлтый", "зелёный", "жёлтый"], [7, 2, 10, 2])

    def running(self):
        print("Светофор включился!")
        for mode in cycle(TrafficLight.__color):
            print(f"\nГорит {mode[0]}", end="")
            for sec in range(mode[1]):
                time.sleep(1)
                print("...", end="")


svetofor = TrafficLight()
svetofor.running()










