# 3. Реализовать функцию, которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))


def my_func(num1, num2, num3):
    return sum(sorted([num1, num2, num3])[-2:])


print(my_func(first, second, third))


