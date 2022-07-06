# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Inventory(object):

    def __init__(self, title):
        self.title = title


class OfficeEquipment(object):

    def __init__(self, equipment_type: str, manufacturer: str, model: str, serial_number: str):
        self.equipment_type = equipment_type
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number


class Printer(OfficeEquipment):

    def __init__(self, manufacturer: str, model: str, serial_number: str, pages_printed: int,
                 color_printer: bool, equipment_type='Printer'):
        super().__init__(equipment_type, manufacturer, model, serial_number)
        self.pages_printed = pages_printed
        self.color_printer = color_printer


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer: str, model: str, serial_number: str, duplex: bool, scan_speed: float,
                 equipment_type='Scanner'):
        super().__init__(equipment_type, manufacturer, model, serial_number)
        self.scan_speed = scan_speed
        self.duplex = duplex


class Copier(OfficeEquipment):
    def __init__(self, manufacturer: str, model: str, serial_number: str, color_copier: bool, copy_speed: float,
                 equipment_type='Copier'):
        super().__init__(equipment_type, manufacturer, model, serial_number)

        self.color_copier = color_copier
        self.copy_speed = copy_speed


if __name__ == "__main__":
    printer = Printer("Xerox", "PH1376", "ST3857NHY", 100, True)
    print(printer.color_printer)
    print(printer.manufacturer)
    print(printer.equipment_type)
    print("*" * 80)
    scanner = Scanner("Samsung", "SM2358", "SN324i3265", True, 10.3)
    print(scanner.manufacturer)
    print("*" * 80)
    copier = Copier("Xerox", "SH3575", "DN358205678", False, 10.09)
    print(copier.manufacturer)
