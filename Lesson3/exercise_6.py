# 6. Реализовать функцию int_func(), принимающую слово из маленьких  букв и возвращающую с прописной первой буквой.
# Если я правильно понял, то метод title() здесь использовать не следует.

def int_func(text):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return text.replace(text[0], letters[letters.index(text[0]) + int(len(letters) / 2)], 1)


user_input = input("Введите строку из слов в нижнем регистре на латинской раскладке, разделённых пробелом: ")
print(" ".join(list(map(int_func, user_input.split()))))
