
# 1. Разные переменные:

integer = 5
fraction = 10 / 4
boolean = True
name = input("What's your name? ")
age = int(input("How old are you? "))
place = input("What place are you from? ")
print(f"{name} from {place}, you were born in {2021 - age}!")

# 2. Перевод времени из секунд в чч:мм:сс:

time_in_secs = int(input("Input time in secs:\n"))
print(f"That would be {time_in_secs // 3600}:{(time_in_secs % 3600) // 60}:{time_in_secs % 60}")

# 3. Сумма чисел n + nn + nnn:

n = int(input("Input any digit from 0 to 9 (n): "))
print("n + nn + nnn = {}".format(123 * n))

# 4. Самая большая цифра в натуральном числе:
nat_number = int(input("Input any natural number: "))
largest_digit = 0
modulo = 0
while nat_number > 0:
    modulo = nat_number % 10
    nat_number = int((nat_number - modulo) / 10)
    if modulo > largest_digit: largest_digit = modulo
print(largest_digit)

# 5. Финансовые результаты фирмы:
gain = int(input("Какова прибыль вашей фирмы?\n"))
costs = int(input("Каковы издержки вашей фирмы?\n"))
if gain > costs:
    profit = gain - costs
    print(f"Вы работаете с прибылью {profit}")
    print(f"Рентабельность вашей фирмы {(profit / gain * 100):.2f}%")
    num_workers = int(input("Какова численность сотрудников вашей фирмы?\n"))
    print(f"прибыль фирмы в расчёте на одного сотрудника: {(profit / num_workers):.2f}")
else:
    print(f"Вы работаете с убытками {costs - gain}")

# 6. Расчёт дня достижения цели спортсменом:
current_dist = int(input("Сколько км вы пробегаете на сегодняшний день?\n"))
target_dist = int(input("К какому результату в км вы стремитесь?\n"))
day_count = 1
while current_dist < target_dist:
    day_count += 1
    current_dist = current_dist * 1.1
print(f"Вы достигнете цели на {day_count}-й день.")
