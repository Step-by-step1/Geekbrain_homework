# 5. Реализовать класс Stationery (канцелярская принадлежность).
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title} не стирается")


class Pencil(Stationery):

    def draw(self):
        print(f"{self.title} хорош для рисования")


class Handle(Stationery):

    def draw(self):
        print(f"{self.title} выдохнется, если забыть закрыть его!")


brush = Stationery("Кисточка")
blue_pen = Pen("Шариковая ручка")
sharpy = Pencil("Твёрдый карандаш")
marker = Handle("Перманентный маркер")

brush.draw()
blue_pen.draw()
sharpy.draw()
marker.draw()
