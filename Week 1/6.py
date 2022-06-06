#6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке. Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
try:
    profit = float(input("Введите значение выручки: "))
    expenses = float(input("Введите значение издержек: "))

    if profit > expenses:
        print(f"Прибыль больше издержек на {profit - expenses}")
        profitability = profit / (profit - expenses)
        print(f"Рентабельность выручки составляет: {round(profitability, 4)} или {round(profitability * 100, 2)}%")
        people = int(input("Введите численность сотрудников фирмы: "))
        profit_per_person = profit / people
        print(f"Прибыль фирмы в расчёте на одного сотрудника: {profit_per_person}")
    elif profit < expenses:
        print(f"Издержки больше прибыли на {expenses - profit}")
    else:
        print("Вы работаете без прибыли и без издержек")
except ValueError:
    print("Введены данные не в числовом формате")