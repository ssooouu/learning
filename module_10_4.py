import random
import threading
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.run = random.randint(3, 10)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        c = 0
        while c != 11:
            for table in self.tables:
                if table.guest is None:
                    print(table.number)
                    table.guest = guests[c]
                    print(f'{guests[c].name} сел(-а) за стол номер {table.number}')
                    th = threading.Thread(target=Cafe, args=(self.queue,))
                    th.start()
                    c += 1

                elif table.guest is not None:
                    print(table.number)
                    self.queue.put(guests[c])
                    print(f'{guests[c].name} в очереди')
                    c += 1
#     self.queue.put(guests[c])
    #                    ~~~~~~^^^
    # IndexError: tuple index out of range
    # После guest_arrival выдает эту ошибку. Я не до конца понимаю что я делаю не так и как запустить поток.
    # Подскажите пожалуйста
    def discuss_guests(self):
        pass


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

