# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


def write_input_to_file(filename) -> None:
    with open(filename, "w") as file:
        while True:
            text = input("Введите данные для записи в файл: > ")
            if text != "":
                file.write(f"{text}\n")
            else:
                break


write_input_to_file("text2.txt")