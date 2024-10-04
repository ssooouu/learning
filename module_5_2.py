class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # print(self.name, self.number_of_floors)


    def go_to(self, new_floors):
        if new_floors < 1 or new_floors > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            c = 0
            while c < new_floors:
                c = c + 1
                print(c)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return  f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
