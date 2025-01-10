import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 1
        while self.enemy != 0:
            self.enemy -= self.power
            print(f'{self.name} сражается {day} дней, осталось {self.enemy} воинов.')
            day += 1
        print(f'{self.name} одержал победу спустя {day - 1} дней!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения

