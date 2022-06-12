# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.
from itertools import count, cycle
lst = list(range(0, 201, 20))


def iterator_from_to(start: int, end:int) -> None:
    for el in count(start):
        if el > end:
            break
        print(el, end=' ')
    print()


def cycle_list(data: list, end: int = 200) -> None:
    cntr = 0
    for el in cycle(data):
        if cntr > end:
            break
        cntr += 1
        print(el, end=' ')


iterator_from_to(3, 10)
cycle_list(lst, 30)
