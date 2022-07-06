# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте
# экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber(object):

    def __init__(self, r, i):
        # real part
        self.r = r
        # imaginary part
        self.i = i

    def __add__(self, other):
        return complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return complex(self.r * other.r, self.i * other.i)


if __name__ == "__main__":
    num1 = ComplexNumber(1, 5)
    num2 = ComplexNumber(3, 8)
    print(num1 + num2)
    print(num1 * num2)
