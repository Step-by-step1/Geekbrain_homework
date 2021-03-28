# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from sys import argv
from itertools import count, cycle
file_name, first_num, cycle_repetitions = argv


geekbrains = "geekbrains"

for el in count(int(first_num)):
    if el >= int(cycle_repetitions) + int(first_num):
        break
    print(el, end=" ")


counter = 0
for el in cycle(geekbrains):
    if counter >= int(cycle_repetitions) * len(geekbrains):
        break
    print(el, end='')
    counter += 1

