# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def greater_than_previous(lst):
    previous = None
    for el in lst:
        if previous is None:
            previous = el
            continue
        elif el > previous:
            yield el
        previous = el


greater_than_previous_list = list(greater_than_previous(data))
print(greater_than_previous_list)
