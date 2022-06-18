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

    def running(self):
        while True:
            timing = time.time()
            if 0 <= time.time() - timing <= self.red_duration:
                self.red()
            elif self.red_duration < time.time() - timing <= self.red_duration + self.yellow_duration:
                self.yellow()
            elif self.red_duration + self.yellow_duration < time.time() - timing <= self.red_duration + self.yellow_duration + self.green_duration:
                self.green()

    def green(self):
        self.__color = 'green'
        print(self.__color)

    def red(self):
        self.__color = 'red'
        print(self.__color)

    def yellow(self):
        self.__color = 'yellow'
        print(self.__color)

