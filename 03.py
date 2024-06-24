class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides, filled=False):
        self.__sides = self.__set_sides_count(sides)
        self.__color = color
        self._filled = filled

    def __set_sides_count(self, *sides):
        if len(sides[0]) > 1:
            return [1 for _ in range(self.sides_count)]
        else:
            return [sides[0][0] for _ in range(self.sides_count)]

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(map(lambda a: 0 <= a <= 255, (r, g, b)))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def set_sides(self, *sides):

        if self.__is_valid_sides(sides):

            sides_tmp = []
            for side in sides:
                if not isinstance(side, int) or side < 0:
                    sides_tmp.clear()
                    break
                else:
                    sides_tmp.append(side)

            if sides_tmp:
                self.__sides = sides_tmp


    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        return all((map(lambda a: a > 0, *sides))) and self.sides_count == len(sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1


class Triangle(Figure):
    sides_count = 3


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
