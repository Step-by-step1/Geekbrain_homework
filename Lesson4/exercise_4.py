# 4. Определить элементы списка, не имеющие повторений.
source_list = []
while True:
    new_num = input("Введите следующий номер или '*' для завершения формирования списка: ")
    if new_num == '*':
        break
    source_list.append(int(new_num))
print(f"Исходный список: {source_list}")
new_list = [el for el in source_list if source_list.count(el) == 1]
print(f"Список на  выходе: {new_list}")
