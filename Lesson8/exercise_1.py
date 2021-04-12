# 1. Реализовать класс «Дата»
class Date:
    def __init__(self, date_as_str):
        self.date_as_str = date_as_str

    @classmethod
    def digitize(cls, date_as_str):
        return list(map(int, date_as_str.split("-")))

    @staticmethod
    def validate(date_as_list):
        days_in_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if date_as_list[1] not in days_in_months.keys():
            print(f"Некорректное значение месяца: {date_as_list[1]}")
            return [None, None, None]
        elif date_as_list[0] not in range(1, days_in_months[date_as_list[1]] + 1):
            print(f"Некорректное значение числа: {date_as_list[0]}")
            return [None, None, None]
        elif date_as_list[2] not in range(3000):
            print(f"Некорректное значение года: {date_as_list[2]}")
            return [None, None, None]
        else:
            return date_as_list

    def day(self):
        return Date.validate(self.digitize(self.date_as_str))[0]

    def month(self):
        return Date.validate(self.digitize(self.date_as_str))[1]

    def year(self):
        return Date.validate(self.digitize(self.date_as_str))[2]


day1 = Date("12-10-1995")
day2 = Date("41-10-2000")
print(day1.day())
print(day2.year())
