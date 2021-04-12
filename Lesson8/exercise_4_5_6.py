# 4,5,6: "Склад оргтехники"

class ExceededCapacityException(Exception):
    """Исключение для случая, когда пытаемся поместить на склад больше техники, чем позволяет доступный объём"""
    def __init__(self, text):
        self.text = text


class WrongObjectException(Exception):
    """Исключение для случая, если пытаемся загрузить или выгрузить объект, не являющимся дочерним от оргтехники"""
    def __init__(self, text):
        self.text = text


class WrongQuantityInputError(Exception):
    """Исключение для случая, если вводим некорректное значение количества техники для загрузки или отгрузки"""
    def __init__(self, text):
        self.text = text


class InsufficientStockError(Exception):
    """Исключение для случая если пытаемся выгрузить больше техники заданного типа, чем есть в наличии на складе"""
    def __init__(self, text):
        self.text = text


class Warehouse:
    """Класс склада"""
    def __init__(self, ttl_capacity, storage=None, history=None):
        """ttl_capacity - максимальная вместимомть склада;
           rem_capacity - остаточная вместимость склада после погрузки / выгрузки техники;
           storage - словарь словарей для хранения информации о технике, находящейся на складе;
           history - словарь словарей для хранения истории отгрузки техники со склада"""
        self.ttl_capacity = ttl_capacity
        self.rem_capacity = ttl_capacity
        self.storage = storage if storage else {}
        self.history = history if history else {}

    def check_capacity(self, item, quantity):
        """Метод для проверки доступного места на складе при погрузке техники"""
        batch_volume = item.unit_volume * quantity
        if self.rem_capacity < batch_volume:
            raise ExceededCapacityException(f"Превышена вместимость склада. Невозможно принять данную партию: {item.model}: {quantity}")
        else:
            self.rem_capacity -= item.unit_volume * quantity

    def receive(self, item, quantity):
        """Метод для погрузки техники на склад и занесения изменений в атрибуты storage и  rem_capacity"""
        try:
            if not type(item) in OfficeAppliance.__subclasses__():
                raise WrongObjectException("Данный экземпляр не относится к классу офисной техники (OfficeAppliance). "
                                           "Перепроверьте данные")
            if not (type(quantity) == int and quantity > 0):
                raise WrongQuantityInputError("Количество техники должно быть задано натуральным числом.")
            if self.storage.get(item.class_name()):
                if self.storage[item.class_name()].get(item.maker):
                    if self.storage[item.class_name()][item.maker].get(item.model):
                        self.storage[item.class_name()][item.maker][item.model] += quantity
                    else:
                        self.storage[item.class_name()][item.maker][item.model] = quantity
                else:
                    self.storage[item.class_name()][item.maker] = {item.model: quantity}
                self.check_capacity(item, quantity)
            else:
                self.storage[item.class_name()] = {item.maker: {item.model: quantity}}
                self.check_capacity(item, quantity)
        except WrongObjectException as err:
            print(err)
        except ExceededCapacityException as err:
            print(err)
        except WrongQuantityInputError as err:
            print(err)

    def dispatch(self, branch, item, quantity):
        """Метод для выгрузки техники со склада с внесением изменений в атрибуты history, storage и rem_capacity"""
        try:
            if not type(item) in OfficeAppliance.__subclasses__():
                raise WrongObjectException("Данный экземпляр не относится к классу офисной техники (OfficeAppliance)."
                                           "Перепроверьте данные")
            if not (type(quantity) == int and quantity > 0):
                raise WrongQuantityInputError("Количество техники должно быть задано натуральным числом.")
            if self.storage.get(item.class_name()):
                if self.storage[item.class_name()].get(item.maker):
                    if self.storage[item.class_name()][item.maker].get(item.model):
                        if self.storage[item.class_name()][item.maker][item.model] >= quantity:
                            self.storage[item.class_name()][item.maker][item.model] -= quantity
                            self.update_history(branch, item, quantity)
                        else:
                            raise InsufficientStockError(f"Запрашиваемое количество {item.class_name()} {item.maker} {item.model} - ({quantity})"
                                  f" превышает имеющееся на складе - ({self.storage[item.class_name()][item.maker][item.model]} задайте приемлемый объём партии.")
                    else:
                        print("На складе нет в наличии устройств данной модели")
                else:
                    print("На складе нет в наличии устройств данного производителя")
            else:
                print(f"На складе нет в наличии устройств типа {item.class_name()}")
            self.storage = Warehouse.check_storage(self.storage)
            self.rem_capacity += quantity * item.unit_volume
        except WrongObjectException as err:
            print(err)
        except WrongQuantityInputError as err:
            print(err)
        except InsufficientStockError as err:
            print(err)

    def update_history(self, branch, item, quantity):
        """Вспомогательный метод для внесения изменений в атрибут history при выгрузке товара"""
        if self.history.get(branch):
            if self.history[branch].get(item.class_name()):
                if self.history[branch][item.class_name()].get(item.maker):
                    if self.history[branch][item.class_name()][item.maker].get(item.model):
                        self.history[branch][item.class_name()][item.maker][item.model] += quantity
                    else:
                        self.history[branch][item.class_name()][item.maker][item.model] = quantity
                else:
                    self.history[branch][item.class_name()][item.maker] = {item.model: quantity}
            else:
                self.history[branch][item.class_name()] = {item.maker: {item.model: quantity}}
        else:
            self.history[branch] = {item.class_name(): {item.maker: {item.model: quantity}}}

    @staticmethod
    def check_storage(dct):
        """Вспомогательный метод для внесения изменений в атрибут storage при выгрузке товара"""
        if all([type(val) == int for val in dct.values()]):
            new_dct = {key: val for key, val in dct.items() if val}
        else:
            new_dct = {key: Warehouse.check_storage(val) for key, val in dct.items() if Warehouse.check_storage(val)}
        return new_dct


class OfficeAppliance:
    """Базовый класс для оргтехники"""
    def __init__(self, maker, model, box_length, box_width, box_height):
        self.maker = maker
        self.model = model
        self.box_length = box_length
        self.box_width = box_width
        self.box_height = box_height
        self.unit_volume = box_length * box_width * box_height

    @classmethod
    def class_name(cls):
        """Этот метод используется для формирования атрибутов storage и history класса Warehouse"""
        return cls.__name__

    @classmethod
    def parent_name(cls):
        """Этот метод используется для валидации ввода экземпляров оргтехники при погрузке / выгрузке"""
        return cls.__bases__[0]


class Printer(OfficeAppliance):
    """Подкласс для принтера"""
    def __init__(self, maker, model, box_length, box_width, box_height, laser=False, inkjet=False):
        super().__init__(maker, model, box_length, box_width, box_height)
        self.laser = laser
        self.inkjet = inkjet


class Scanner(OfficeAppliance):
    """Подкласс для сканера"""
    def __init__(self, maker, model, box_length, box_width, box_height, flatbed=False, sheet_fed=False, drum=False):
        super().__init__(maker, model, box_length, box_width, box_height)
        self.flatbed = flatbed
        self.sheet_fed = sheet_fed
        self.drum = drum


class Copier(OfficeAppliance):
    """Подкласс для копировальной машины"""
    def __init__(self, maker, model, box_length, box_width, box_height, colour=False, a4=False, a3=False):
        super().__init__(maker, model, box_length, box_width, box_height)
        self.colour = colour
        self.a4 = a4
        self.a3 = a3


# Создаём экземпляры оргтехники
print1 = Printer("Canon", "first", 1, 2, 3)
print2 = Printer("Canon", "second", 1, 1, 1)
print3 = Printer("Brother", "uno", 1, 3, 2)
print4 = Printer("Brother", "dos", 2, 1, 1)
scan1 = Scanner("Canon", "scan1", 2, 2, 2)
scan2 = Scanner("Canon", "scan2", 1, 3, 1)
scan3 = Scanner("Sony", "sc1", 1, 1, 1)
scan4 = Scanner("Sony", "sc2", 2, 1, 2)
cop1 = Copier("Brother", "c1", 2, 1, 3)
cop2 = Copier("Brother", "c2", 2, 3, 1)
cop3 = Copier("Dell", "1", 1, 1, 3)
cop4 = Copier("Dell", "2", 2, 2, 2)

# Создаём экземпляр склада с вместимостью 200
wh = Warehouse(200)
# Загружаем технику на склад.
wh.receive(print1, 1)
# Проверим валидацию ввода количества техники, введя ненатуральное число
wh.receive(print4, 5.1)
wh.receive(print4, 5)
wh.receive(print1, 7)
wh.receive(print2, 3)
wh.receive(print3, 1)
wh.receive(print4, 9)
wh.receive(print1, 3)
# Проверим валидацию ввода экземпляра техники, введя строковое значение
wh.receive("scan1", 3)
wh.receive(scan1, 4)
wh.receive(scan2, 2)
wh.receive(scan3, 5)
wh.receive(scan4, 1)
wh.receive(cop1, 5)
# Проверим отработку исключения ExceededCapacityException, введя количество техники, объём которой превышает допустимый
wh.receive(cop2, 6)
wh.receive(cop3, 2)
wh.receive(cop4, 6)

print(f"Техника на складе: {wh.storage}")
print(f"Остаточная вместимость склада: {wh.rem_capacity}")
print('\n\n\n\n*******')

# Отправляем технику со склада по отделениям компании (Accounting, Manning, Purchasing)
wh.dispatch("Accounting", print1, 11)
# Проверим отработку исключения InsufficientStockError, введя количество превышающее то, которое имеется на складе
wh.dispatch("Manning", print2, 4)
wh.dispatch("Manning", print2, 3)
wh.dispatch("Accounting", scan1, 3)
wh.dispatch("Purchasing", scan2, 2)
# Проверим валидацию ввода количества техники, введя ненатуральное число
wh.dispatch("Accounting", cop1, -3)
# Проверим валидацию ввода экземпляра техники, введя строковое значение
wh.dispatch("Accounting", "cop1", 3)
wh.dispatch("Accounting", cop1, 3)

print(f"Техника на складе поле отправки: {wh.storage}")
print(f"История отправок техники со склада: {wh.history}")
print(f"Остаточная вместимость склада: {wh.rem_capacity}")
