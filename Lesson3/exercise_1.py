# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
dividend = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))


def division_func(num1, num2):
    if num2 != 0:
        return num1 / num2
    return "Деление на ноль не может быть выполнено!"


print(division_func(dividend, divider))
