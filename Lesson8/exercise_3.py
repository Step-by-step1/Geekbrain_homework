# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
class NotDigitError(Exception):
    def __init__(self, text):
        self.text = text


value = None
my_list = []
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while value != "stop":
    try:
        value = input("Введите следующее значение в список или 'stop' для завершения формирования списка:")
        if value[0] in ["+", "-"]:
            plus_or_minus = value[0]
            value1 = value[1:]
        else:
            plus_or_minus = ""
            value1 = value
        if not (len(value1.split(".")) < 3 and all([all([symb in num_list for symb in el]) for el in value1.split(".")])):
            raise NotDigitError("Вы ввели нечисловое значение. Только числа добавляются в список.")
        value = float(plus_or_minus + value1)
    except NotDigitError as err:
        if not (plus_or_minus + value1) == "stop":
            print(err)
    else:
        my_list.append(value)

print(my_list)
