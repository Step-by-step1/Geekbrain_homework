# Реализовать структуру «Рейтинг»:
rating = [7, 5, 3, 3, 2]
print(f'Начальные рейтинг: {rating}')
number = int(input("Введите любое натуральное число: "))
rating.append(number)
rating.sort(reverse=True)
print(f'Обновлённый рейтинг: {rating}')
