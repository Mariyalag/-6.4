
class Figure:
    sides_count = 0

    def __init__(self,  color, *sides):
        self.__color = color
        self.filled = False
        if not self.__is_valid_sides(*sides):
            self._sides = [1] * self.sides_count
        else:
            self._sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value < 256 for value in [r, g, b])

    def set_color(self, *color):
        if len(color) == 3 and self.__is_valid_color(*color):
            self.__color = color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius * 2)

    def get_square(self):
        return 3.14 * (self._sides[0] ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self._sides
        p = sum(self._sides) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, [side_length] * 12)

    def get_volume(self):
        return self._sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())