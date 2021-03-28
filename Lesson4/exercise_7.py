# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
number = int(input("Введите число n: "))


def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x


for el in fact(number):
    print(el, end=" ")

