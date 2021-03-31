# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
with open("exercise_1.txt", "w") as text_file:
    while True:
        new_row = input("Введите новую строку: ")
        if new_row == "":
            break
        text_file.write(new_row + "\n")

