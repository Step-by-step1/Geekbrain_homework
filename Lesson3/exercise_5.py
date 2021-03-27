# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма.
def summarize(text, old_sum):
    old_sum += sum(list(map(int, text.split('*')[0].split())))
    print(f'Итоговая сумма: {old_sum}')
    return old_sum, '*' in text


new_sum = 0
stop_word = None
while not stop_word:
    user_input = input("Введите строку чисел, разделённых пробелом. Введите '*' для того, чтобы завершить программу: ")
    new_sum, stop_word = summarize(user_input, new_sum)



