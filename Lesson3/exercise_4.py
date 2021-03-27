# 4. Необходимо выполнить возведение числа x в степень y.
number = float(input("Введите положительное действительное число: "))
power = int(input("Введите отрицательное целое число: "))


def my_func(x, y):
    result = 1
    for i in range(abs(y)): result *= x
    return 1 / result


print(my_func(number, power))
