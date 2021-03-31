# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
import json
total_profit = 0
profit_counter = 0
my_list = [{}, {}]
with open("exercise_7.txt") as firms:
    for line in firms:
        line_lst = line.split()
        firm = line_lst[0]
        profit = int(line_lst[-2]) - int(line_lst[-1])
        if profit > 0:
            total_profit += profit
            profit_counter += 1
        my_list[0][firm] = profit
my_list[1]["average_profit"] = total_profit / profit_counter
print(my_list)
with open("exercise_7.json", "w") as json_file:
    json.dump(my_list, json_file)



