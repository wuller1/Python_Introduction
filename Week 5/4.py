# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

filename = "text4.txt"
filename_out = "text4-out.txt"
russian_dict = {
                "One": "Один",
                "Two": "Два",
                "Three": "Три",
                "Four": "Четыре"
                }


def read_file_change_numeric(input_file: str, output_file: str) -> None:
    with open(filename, encoding="UTF-8") as input_text:
        for line in input_text:
            line_list = line.split(" ")
            line_list[0] = russian_dict[line_list[0]]
            out_line = " ".join(line_list)

            with open(filename_out, "a", encoding="UTF-8") as out_file:
                out_file.write(out_line)


read_file_change_numeric(filename, filename_out)
