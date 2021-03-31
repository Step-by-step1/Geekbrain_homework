# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
with open("exercise_3.txt") as text_file:
    line_count = 0
    total_salary = 0
    for line in text_file:
        name = line.split()[0]
        salary = int(line.split()[-2])
        if salary < 20000:
            print(f"{name} получает всего лишь {salary} рублей!")
        total_salary += salary
        line_count += 1
    print(f"\nСредний заработок сотрудников: {total_salary / line_count} рублей.")

