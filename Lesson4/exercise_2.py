# 2. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
source_list = []
while True:
    new_num = input("Введите следующий номер или '*' для завершения формирования списка: ")
    if new_num == '*':
        break
    source_list.append(int(new_num))
print(f"Исходный список: {source_list}")
new_list = [source_list[i] for i in range(1,len(source_list) - 1) if source_list[i] > source_list[i - 1]]
print(f"Список на выходе: {new_list}")

