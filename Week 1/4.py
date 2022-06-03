num = input("Введите число: ")
i = 0
max_num = 0

while i < len(num):
    if int(num[i]) > max_num:
        max_num = int(num[i])
    i += 1

print(max_num)
