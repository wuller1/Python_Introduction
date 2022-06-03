try:
    sec = int(input("Введите время в секундах: "))
    hours = int(sec / 3600)
    minutes = int((sec - (hours * 3600)) / 60)
    seconds = sec - hours * 3600 - minutes * 60

    if hours < 10:
        hours = "0" + str(hours)

    if minutes < 10:
        minutes = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    print(f"{hours}:{minutes}:{seconds}")
except ValueError:
    print("Невозможно перевести во временной формат")