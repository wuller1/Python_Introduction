# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
from statistics import mean
from json import dump
pathname = "text7.txt"


def calculate_profit(path):
    profit_dict = {}
    profit_list = []
    json_list = []
    with open(path, encoding="UTF-8") as file:
        for line in file:
            firm_list = line.rstrip().split(" ")
            firm_profit = float(firm_list[2]) - float(firm_list[3])
            profit_dict[firm_list[0]] = firm_profit
        json_list.append(profit_dict)

        for item in profit_dict.values():
            if item >= 0:
                profit_list.append(item)
        mean_profit = mean(profit_list)
        json_list.append({"average_profit": round(mean_profit, 2)})
        with open("json_data.json", "w") as json_file:
            dump(json_list, json_file)


calculate_profit(pathname)
