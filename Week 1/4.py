#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
try:
    num = input("Введите число: ")
    i = 0
    max_num = 0

    while i < len(num):
        if int(num[i]) > max_num:
            max_num = int(num[i])
        i += 1

    print(max_num)
except ValueError:
    print("Введены данные не в числовом формате")