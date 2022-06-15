# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
file_path = "text6.txt"


def parse_file(path):
    output_dictionary = {}
    with open(path, encoding="UTF-8") as file:
        for line in file:
            line_list = line.rstrip().split("-")
            i = 0
            line_sum = 0
            while i < len(line_list):
                if i == 0:
                    line_list[i] = line_list[i][:-1]
                else:
                    position = line_list[i].find("(")
                    if position != -1:
                        line_list[i] = line_list[i][:position]
                i += 1
            for item in line_list:
                if item.isnumeric():
                    line_sum += int(item)

            output_dictionary[line_list[0]] = line_sum
    print(output_dictionary)


parse_file(file_path)
