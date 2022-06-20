# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car(object):

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    @staticmethod
    def go():
        return "Машина поехала вперед"

    @staticmethod
    def stop():
        return "Машина остановилась"

    @staticmethod
    def turn(direction):
        return f"Машина повернула {direction}"

    def show_speed(self):
        return f"Текущая скорость автомобиля: {self.speed} км/ч"


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            return f"Вы превысили скорость на {self.speed - self.speed_limit} км/ч, ваша скорость {self.speed} км/ч"


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            return f"Вы превысили скорость на {self.speed - self.speed_limit} км/ч, ваша скорость {self.speed} км/ч"


class PoliceCar(Car):
    pass


if __name__ == "__main__":
    # SportCar
    print("*" * 80)
    print("The SportCar class")
    print("*" * 80)
    sport_car = SportCar(300, "красный", "Lamborghini", False)
    print(sport_car.show_speed())
    print(sport_car.name)
    print(sport_car.speed)
    print(sport_car.color)
    print(sport_car.is_police)
    print(sport_car.go())
    print(sport_car.turn('направо'))
    print(sport_car.stop())
    # TownCar
    print("*" * 80)
    print("The TownCar class")
    print("*" * 80)
    town_car = TownCar(70, "зеленый", "Nissan Leaf", False)
    print(town_car.show_speed())
    print(town_car.name)
    print(town_car.speed)
    print(town_car.color)
    print(town_car.is_police)
    print(town_car.go())
    print(town_car.turn('налево'))
    print(town_car.stop())
    # Car
    print("*" * 80)
    print("The Car class")
    print("*" * 80)
    car = Car(120, "черный", "Honda Fit", False)
    print(car.show_speed())
    print(car.name)
    print(car.speed)
    print(car.color)
    print(car.is_police)
    print(car.go())
    print(car.turn('направо'))
    print(car.stop())
    # WorkCar
    print("*" * 80)
    print("The WorkCar class")
    print("*" * 80)
    work_car = WorkCar(90, "оранжевый", "Honda Fit", False)
    print(work_car.show_speed())
    print(work_car.name)
    print(work_car.speed)
    print(work_car.color)
    print(work_car.is_police)
    print(work_car.go())
    print(work_car.turn('направо'))
    print(work_car.stop())
    # PoliceCar
    print("*" * 80)
    print("The PoliceCar class")
    print("*" * 80)
    police_car = PoliceCar(90, "оранжевый", "Honda Fit", True)
    print(police_car.show_speed())
    print(police_car.name)
    print(police_car.speed)
    print(police_car.color)
    print(police_car.is_police)
    print(police_car.go())
    print(police_car.turn('направо'))
    print(police_car.stop())
