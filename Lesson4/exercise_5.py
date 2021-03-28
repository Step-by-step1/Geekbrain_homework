# 5. Получить результат вычисления произведения всех элементов списка.
from functools import reduce
source_list = [el for el in range(100, 1001) if el % 2 == 0]
print(source_list)


def multiplication(num1, num2):
    return num1 * num2


print(reduce(multiplication, source_list))




