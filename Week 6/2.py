# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road(object):
    coefficient = 25

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def calculate_mass(self):
        return self._length * self._width * self._height * self.coefficient


if __name__ == "__main__":
    road = Road(5000, 20, 5)
    print(road.calculate_mass())
