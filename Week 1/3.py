# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
try:
    num = input("Введите положительное число: ")

    num1 = int(num)
    num2 = int(num + num)
    num3 = int(num + num + num)

    num_sum = num1 + num2 + num3

    print(num_sum)
except ValueError:
    print("Введены данные не в числовом формате")