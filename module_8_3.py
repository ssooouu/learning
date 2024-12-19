class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info
    

class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.vin = __vin
        self.num = __numbers
        self.__is_valid_vin(self.vin)
        self.__is_valid_numbers(self.num)


    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, float):
            raise IncorrectVinNumber('Некорректный тип VinNumber', 'VinNumber должен быть целым числом')
        if 9999999 > vin_number < 1000000:
            raise IncorrectVinNumber('Некорректный тип VinNumber', 'VinNumber должен быть от 1000000 до 9999999')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        flag = isinstance(numbers, str)
        count = 0
        for i in numbers:
            count += 1
        if not flag:
            raise IncorrectCarNumbers('Некорректный тип CarNumbers', 'CarNumbers должен быть строкой')
        if count != 6:
            raise IncorrectCarNumbers('Некорректный тип CarNumbers', 'CarNumbers должен состоять из 6 символов')
        else:
            return True



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
