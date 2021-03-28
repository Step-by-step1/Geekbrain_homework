# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
from sys import argv
file_name, hours_worked, pay_per_hour, premium = argv


def total_pay(hours, pay, prem):
    return hours * pay + prem


print(total_pay(int(hours_worked), int(pay_per_hour), int(premium)))


