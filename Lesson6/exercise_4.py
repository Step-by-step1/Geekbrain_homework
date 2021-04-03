# 4. Реализуйте базовый класс Car.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала!")

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановилась!")

    def turn(self, direction):
        print(f"{self.name} поворачивает {direction}!")

    def show_speed(self):
        print(f"{self.name} движется со скоростью {self.speed} км/ч!")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"А это - превышение скорости на {self.speed - 60} км/ч!")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"А это - превышение скорости на {self.speed - 40} км/ч!")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


sport = SportCar(90, "red", "Audi", False)
print(f"Спортивная машина: {sport.name}")
sport.go()
sport.turn("влево")
police = PoliceCar(60, "белая", "Лада")
print(f"{police.color.title()} {police.name} - полицейская машина: {police.is_police}")
police.turn("вправо")
police.stop()
police.show_speed()
town = TownCar(80, "серый", "Prius", False)
town.show_speed()
work = WorkCar(70, "коричневая", "Mazda", False)
work.show_speed()

