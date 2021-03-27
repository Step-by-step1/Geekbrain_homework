# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки:
user_string = input("Веведите строку: ")
lst = user_string.split()
for num, string in enumerate(lst): print(num, string[:10])
