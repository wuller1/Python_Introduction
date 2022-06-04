# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное,
# выводить только первые 10 букв в слове.

data = input("Введите слова, разделяя их пробелом: ")

for key, word in enumerate(data.split(" ")):
    if len(word) < 10:
        print(f"Слово {key + 1}: {word}")
    else:
        print(f"Слово {key + 1}: {word[:10]}")
