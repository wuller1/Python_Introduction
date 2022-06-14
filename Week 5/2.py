# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

def number_of_lines_and_words(filename: str) -> None:
    with open(filename) as txt:
        line_number = 0
        for line in txt:
            line_number += 1
            words_in_line = len(line.split(" "))
            print(f"Строка {line_number}: {words_in_line} слов")

        print("*" * 22)
        print(f"Всего строк в файле: {line_number}")


number_of_lines_and_words("text1.txt")