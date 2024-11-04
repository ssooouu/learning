class Figure:

    def __init__(self, __color, __sides, filled=True):
        self.sides = __sides
        self.color = __color
        self.filled = filled
        self.sides_count = 0

    def get_color(self):
        return self.color

    def set_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.color = (r, g, b)
        else:
            print(f'Нельзя установить цвет: {r, g, b}')

    def __is_valid_sides(self, *new_sides):
        self.new_sides = new_sides
        count_side = 0
        side_cor = True
        for c in new_sides:
            count_side += 1
        for num in new_sides:
            if isinstance(num, float) or num < 0:
                side_cor = False
                break
            else:
                side_cor = True

        if len(self.box_side) == count_side and side_cor == True:
            return True
        else:
            return False

    def get_sides(self):
        return self.box_side

    def __len__(self):
        n = []
        f = 0
        box = []
        for i in self.box_side:
            if isinstance(i, int):
                n.append(i)
        for c in n:
            f += c
        while f > 0:
            box.append(f)
            f -= 1
        return len(box)

    def set_sides(self, *new_sides):
        self.new_side = new_sides
        if Figure.__is_valid_sides(self, *new_sides) == True:
            self.box_side = self.new_side
        else:
            print('Так нельзя')


class Circle(Figure):
    def __init__(self, __color, __sides, filled=True):
        super().__init__(__color, __sides, filled)
        self.sides_count = 1
        self.sides = self.sides * self.sides_count
        self.box_side = []
        coun = self.sides_count
        while coun > 0:
            coun -= 1
            self.box_side.append(self.sides)
        

    def radius(self):
        rad = self.sides / 2 * 3.14
        print(rad, 'я радиус')
        return rad


class Cube(Figure):
    def __init__(self, __color, __sides, filled=True):
        super().__init__(__color, __sides, filled)
        self.sides_count = 12
        self.box_side = []
        coun = self.sides_count
        while coun > 0:
            coun -= 1
            self.box_side.append(self.sides)

    def get_volume(self):
        a = self.sides
        v = a * a * a
        return v


class Triangle(Figure):
    def __init__(self, __color, __sides, filled=True):
        super().__init__(__color, __sides, filled)
        self.sides_count = 3
        self.box_side = []
        coun = self.sides_count
        while coun > 0:
            coun -= 1
            self.box_side.append(self.sides)

    def get_square(self):
        a = self.sides
        square = a * a * 1.73 / 4  # Треугольник равносторонний 1,73 - округления корня из 3
        return square


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
tr = Triangle((200, 200, 200), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# # Проверка объёма (куба):
print(cube1.get_volume())
