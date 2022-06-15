# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
path = "text5.txt"


def create_file_calculate_sum(filename):

    numbers_sum = 0

    with open(filename, "w", encoding="UTF-8") as file:
        file.write("10 20 30 40 50")

    with open(filename, encoding="UTF-8") as file:
        numbers_list = file.readline().split(" ")

        for number in numbers_list:
            numbers_sum += float(number)

    print(numbers_sum)


create_file_calculate_sum(path)
