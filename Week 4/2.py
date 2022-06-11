# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def greater_than_previous(lst):
    previous = None
    new_list = []
    for el in lst:
        if previous is None:
            previous = el
            continue
        elif el > previous:
            new_list.append(el)
        previous = el
    return new_list


print(greater_than_previous(data))
