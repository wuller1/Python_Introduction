# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


if __name__ == "__main__":
    def divide(num_1, num_2):
        try:
            if num_2 == 0:
                raise DivisionByZero("Деление на ноль недопустимо")
            return num_1 / num_2
        except DivisionByZero as err:
            return err


    print(divide(3, 0))
