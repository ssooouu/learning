class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет машины на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_model(self):
        return self.model

    def get_horsepower(self):
        return self.engine_power

    def get_color(self):
        return self.color

    def print_info(self):
        print(f'Модель: {Sedan.get_model(self)}, Мощность двигателя: {Sedan.get_horsepower(self)}, '
                f'Цвет: {Sedan.get_color(self)}, Владелец: {self.owner}')




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
