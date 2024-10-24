class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        if food is True:
            print(f'{self.name}, сьел {food}')
            self.fed = True
        else:
            print(f'{self.name} сьел {food} и умер')
            self.alive = False


class Mammal(Animal):

    def eat(self, food):
        if food.edible is True:
            print(f'{self.name}, сьел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} сьел {food.name} и умер')
            self.alive = False


class Predator(Animal):
    def eat(self, food):
        if food.edible is True:
            print(f'{self.name}, сьел {food}')
            self.fed = True
        else:
            print(f'{self.name} сьел {food} и умер')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

    def __str__(self):
        return self.name


class Flower(Plant):
    zxv = 123


class Fruit(Plant):
    def __init__(self, name, edible = True):
        self.name = name
        self.edible = edible




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
