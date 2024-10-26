class Horse:
    def __init__(self, sound='Frrr', x_distance=0):
        self.sound = sound
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self, sound='I train, eat, sleep, and repeat', y_distance=0):
        self.sound = sound
        self.y_distance = y_distance
        self.a = 10

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Eagle, Horse):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        print(self.x_distance)

    def move(self, dx, dy):
        super().fly(dy)
        super().run(dx)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'{self.sound}')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
