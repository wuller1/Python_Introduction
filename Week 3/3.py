# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(num1: float, num2: float, num3: float) -> float:
    """
    Находит сумму двух наибольших чисел из 3-х

    :param num1: Любое число
    :param num2: Любое число
    :param num3: Любое число
    :return: Сумму двух наибольших чисел
    """
    numbers = (num1, num2, num3)
    minimum = min(*numbers)
    total = 0

    for i in numbers:
        if i != minimum:
            total += i
    return total


print(my_func(3, 11, 18))
