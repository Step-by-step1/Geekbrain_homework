# Обмен значений соседних элементов:
lst = []
while True:
    el = input("Введите следующий элемент списка или введите 'end' чтобы завершить формирование списка: ")
    if el == 'end':
        break
    lst.append(el)
if len(lst) < 2:
    modified_lst = lst
else:
    modified_lst = [lst[i + 1] if i % 2 == 0 else lst[i - 1] for i in range(len(lst) - 1)] + [lst[-(len(lst) % 2)]]
print(modified_lst)
