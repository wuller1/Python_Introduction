# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix(object):
    def __init__(self, *args):
        self.args = args
        length_previous = len(args[0])
        for arg in args:
            if len(arg) != length_previous:
                raise ValueError("Количество элементов должно совпадать")

    def __str__(self):
        stringify = ""
        for el in self.args:
            stringify += f"\n{el}"
        return stringify

    def __add__(self, other):
        row_number = 0
        column_number = 0
        added_matrix = []

        if len(self.args) == len(other.args) and len(self.args[0]) == len(other.args[0]):
            while 0 <= row_number < len(self.args):
                row_temp = []
                while 0 <= column_number < len(self.args[0]):
                    row_temp.append(self.args[row_number][column_number] + other.args[row_number][column_number])
                    column_number += 1
                column_number = 0
                row_number += 1
                added_matrix.append(row_temp)

        else:
            raise ValueError("Размеры матриц для сложения должны совпадать")
        return tuple(added_matrix)


if __name__ == "__main__":
    matrix1 = Matrix([3, 5, 5, 3], [8, 3, 7, 1])
    matrix2 = Matrix([4, 5, 6, 7], [7, 8, 9, 10])
    matrix3 = Matrix(*(matrix1 + matrix2))
    print(str(matrix3))
    print(str(matrix1))
