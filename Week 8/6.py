# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
import datetime


class DataTypeError(Exception):
    def __init__(self, text):
        self.text = text


class Inventory(object):

    def __init__(self, title):
        self.title = title
        self.inventory_registry = []
        self.inventory_log = []

    def store(self, equipment, number):
        try:
            if not isinstance(number, str):
                self.inventory_registry.append({"number": number, **equipment.__dict__})
            else:
                raise DataTypeError("Нельзя использовать строковый тип данных для количества")
        except DataTypeError as err:
            print(err)

    def give_away(self, equipment_id, department, number):
        try:
            if isinstance(number, str):
                raise DataTypeError("Невозможно использовать строковый тип данных для количества")

            update_key = None

            # find key to update
            for key, value in enumerate(self.inventory_registry):
                if value['item_id'] == equipment_id:
                    update_key = key

            # update and write to log
            if update_key is not None and self.inventory_registry[update_key]["number"] >= number:
                self.inventory_registry[update_key]["number"] = self.inventory_registry[update_key]["number"] - number

                self.inventory_log.append({"date": datetime.datetime.now(), "equipment_id": equipment_id,
                                           "department": department, "number": number})
        except DataTypeError as err:
            print(err)


class OfficeEquipment(object):

    def __init__(self, item_id: int, equipment_type: str, manufacturer: str, model: str, serial_number: str):
        self.equipment_type = equipment_type
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.item_id = item_id


class Printer(OfficeEquipment):

    def __init__(self, _id: int, manufacturer: str, model: str, serial_number: str, pages_printed: int,
                 color_printer: bool, equipment_type='Printer'):
        super().__init__(_id, equipment_type, manufacturer, model, serial_number)
        self.pages_printed = pages_printed
        self.color_printer = color_printer


class Scanner(OfficeEquipment):
    def __init__(self, _id: int, manufacturer: str, model: str, serial_number: str, duplex: bool, scan_speed: float,
                 equipment_type='Scanner'):
        super().__init__(_id, equipment_type, manufacturer, model, serial_number)
        self.scan_speed = scan_speed
        self.duplex = duplex


class Copier(OfficeEquipment):
    def __init__(self, _id, manufacturer: str, model: str, serial_number: str, color_copier: bool, copy_speed: float,
                 equipment_type='Copier'):
        super().__init__(_id, equipment_type, manufacturer, model, serial_number)

        self.color_copier = color_copier
        self.copy_speed = copy_speed


if __name__ == "__main__":
    printer = Printer(1, "Xerox", "PH1376", "ST3857NHY", 100, True)
    scanner = Scanner(2, "Samsung", "SM2358", "SN324i3265", True, 10.3)

    inventory = Inventory("First")
    inventory.store(printer, 10)
    inventory.store(scanner, 20)
    print(inventory.inventory_registry)
    inventory.give_away(1, "Economics", 5)
    print(inventory.inventory_registry)
