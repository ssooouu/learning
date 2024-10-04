class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(self.name, self.number_of_floors)


    def go_to(self, new_floors):
        if new_floors < 1 or new_floors > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            c = 0
            while c < new_floors:
                c = c + 1
                print(c)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
