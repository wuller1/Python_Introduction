# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен
# выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery(object):

    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print("Запуск отрисовки")


class Pen(Stationery):

    @staticmethod
    def draw():
        print("Рисую ручкой")


class Pencil(Stationery):

    @staticmethod
    def draw():
        print("Рисую карандашом")


class Handle(Stationery):

    @staticmethod
    def draw():
        print("Рисую маркером")


if __name__ == "__main__":
    stationery = Stationery("Канцелярская принадлежность")
    pen = Pen("Ручка")
    pencil = Pencil("Карандаш")
    handle = Handle("Маркер")
    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()
