try:
    sec = int(input("Введите время в секундах: "))
    print(sec / 360)
except ValueError:
    print("Невозможно перевести во временной формат")

