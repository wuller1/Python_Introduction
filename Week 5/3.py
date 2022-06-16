# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
from statistics import mean


def less_than_twenty_thousand(filename: str) -> None:
    salary_dict = {}
    filtered_dict = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            data = line.split(" ")
            family_name = data[0]
            salary = float(data[1].rstrip())
            salary_dict[family_name] = salary
    for second_name, salary_data in salary_dict.items():
        if salary_data < 20000:
            filtered_dict[second_name] = salary_data

    print("Зарабатывают менее 20000 рублей: ")
    for second_name, salary_data in filtered_dict.items():
        print(second_name)
    print("*" * 25)
    print(f"Средняя заработная плата сотрудников на предприятии: {round(mean(salary_dict.values()), 2)} рублей")


less_than_twenty_thousand("text3.txt")
