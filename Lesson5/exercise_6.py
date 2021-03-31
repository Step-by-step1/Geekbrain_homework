# 6.Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
numbers = "0123456789"
my_dict = {}
with open("exercise_6.txt") as schedule:
    for line in schedule:
        subject = line[:line.index(":")]
        for symb in line:
            if symb not in numbers:
                line = line.replace(symb, " ")
        my_dict[subject] = sum(list(map(int, line.split())))
print(my_dict)
