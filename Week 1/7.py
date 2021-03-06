#7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
try:
    distance_first_day = float(input("Введите результат в первый день: "))
    distance_goal = float(input("Введите вашу цель: "))
    distance = distance_first_day
    day = 1
    print("Результат:")
    print(f"1-й день: {distance_first_day} км")

    while distance < distance_goal:
        day += 1
        distance += distance * 0.1
        print(f"{day}-й день: {round(distance, 2)} км")

    print(f"На {day}-й день спортсмен достиг результата не менее {distance_goal} км.")
except ValueError:
    print("Введены данные не в числовом формате")