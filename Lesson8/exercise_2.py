# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
class MyZeroDivisionErr(Exception):
    def __init__(self, text):
        self.text = text


numer = input("Введите числитель:")
denom = input("Введите знаменатель:")

try:
    denom = float(denom)
    if denom == 0:
        raise MyZeroDivisionErr("Деление на ноль не может быть выполнено")
except ValueError:
    print("Введите числовое значение знаменателя")
except MyZeroDivisionErr as err:
    print(err)
else:
    try:
        numer = float(numer)
    except ValueError:
        print("Введите числовое значение числителя")
    else:
        print(numer / denom)
