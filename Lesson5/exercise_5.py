# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
user_input = input("Введите последовательность чисел, разделённых пробелами: ")
with open("exercise_5.txt", "w+") as text_file:
    text_file.write(user_input)
    text_file.seek(0)
    content = text_file.read()
    print(f"Содержимое созданного файла: {content}")
    num_list = content.split()
    print(f"Сумма всех введённых чисел:{sum(map(int,num_list))}")
