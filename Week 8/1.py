# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date(object):

    def __init__(self, date_string):
        self.date = Date.get_date_month_year(date_string)

    @classmethod
    def get_date_month_year(cls, param):
        date_list = param.split("-")
        date_list_int = [int(x) for x in date_list]
        if cls.validate_date_month_year(date_list_int):
            return tuple(date_list_int)
        else:
            raise ValueError("Некорректный формат даты и времени")

    @staticmethod
    def validate_date_month_year(date_input):
        date_number = date_input[0]
        month = date_input[1]
        year = date_input[2]

        if 0 < date_number < 32 and 0 < month <= 12 and 1900 < year <= 3000:
            return True
        return False


if __name__ == "__main__":
    date = Date("04-07-2022")
    print(date.date)
