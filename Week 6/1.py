# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight(object):
    __color = ''
    red_duration = 7
    yellow_duration = 2
    green_duration = 30
    previous_light = 'yellow'

    def running(self):
        while True:
            self.red()
            self.yellow()
            self.green()

    @staticmethod
    def close_program():
        print("\nНарушен порядок цветовых сигналов, завершаю программу...")
        exit()

    def green(self):
        if self.previous_light == 'yellow':
            self.previous_light = 'green'
            self.__color = 'green'
            print("\r", end="")
            print("🟢", end="")
            time.sleep(self.green_duration)
        else:
            self.close_program()

    def red(self):
        if self.previous_light == 'yellow':
            self.previous_light = 'red'
            self.__color = 'red'
            print("\r", end="")
            print("🔴", end="")
            time.sleep(self.red_duration)
        else:
            self. close_program()

    def yellow(self):
        if self.previous_light == 'red':
            self.previous_light = 'yellow'
            self.__color = 'yellow'
            print("\r", end="")
            print("🟡", end="")
            time.sleep(self.yellow_duration)
        else:
            self.close_program()


if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.running()

