# 2.Выполнить подсчет количества строк, количества слов в каждой строке.
with open("exercise_2.txt") as text_file:
    row_count = 1
    for row in text_file:
        print(f"В {row_count}-й строке {len(row.split())} слов!")
        row_count += 1


