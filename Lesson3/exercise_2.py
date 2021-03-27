# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
user_first_name = input("Введите ваше имя: ")
user_last_name = input("Введите вашу фамилию: ")
user_year_of_birth = input("Введите год вашего рождения: ")
user_place = input("Введите ваш населённый пункт: ")
user_tel = input("Введите номер вашего телефона: ")
user_email = input("Введите ваш электронный почтовый адрес: ")


def users_data(first_name, last_name, year_of_birth, place, tel, email):
    print(f'{first_name.title()} {last_name.title()}, вы родились в {year_of_birth}-м году и проживаете в г.{place.title()}! Номер вашего телефона: {tel}, ваш електронный почтовый адрес: {email}.')


users_data(first_name=user_first_name, last_name=user_last_name, year_of_birth=user_year_of_birth, place=user_place, tel=user_tel, email=user_email)
