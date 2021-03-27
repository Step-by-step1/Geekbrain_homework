# Реализовать структуру данных «Товары»:
lst = []
while True:
    name = input("Введите название товара или введите 'end', чтобы закончить формирование структуры данных: ")
    if name == 'end':
        break
    price = input("Введите цену товара: ")
    quantity = input("Введите количество товара: ")
    unit = input("Введите наименование единицы товара: ")
    lst.append((len(lst) + 1, ({"название": name, "цена": price, "количество": quantity, "ед.": unit})))
if len(lst) < 1:
    print("Вы ничего не ввели")
else:
    print({key: [lst[i][1][key] for i in range(len(lst))] for key in lst[0][1].keys()})
