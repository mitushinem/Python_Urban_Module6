class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides, filled=False):
        self.__sides = self.__get_sides_count(sides)
        self.__color = color
        self._filled = filled

    def __get_sides_count(self, *sides):
        if self.sides_count == len(sides):
            return sides
        else:
            return [1 for _ in range(self.sides_count)]

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(map(lambda a: 0 <= a <= 255, (r, g, b)))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def set_sides(self, *sides):
        sides_tmp = []
        for side in sides:
            if not isinstance(side, int) or side < 0:
                sides_tmp.clear()
                break
            else:
                sides_tmp.append(side)

        if sides_tmp:
            self.__sides = sides_tmp

    def __is_valid_sides(self, *sides):
        return all((map(lambda a: a > 0, *sides))) and self.sides_count == len(sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


class Cube(Figure):
    pass


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
