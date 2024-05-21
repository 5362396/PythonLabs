class Point:
    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'Point({self.x}, {self.y})'

    def __mul__(self, multiplier: int) -> 'Point':
        return Point(self.x * multiplier, self.y * multiplier)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self) -> str:
        return str(self)


class Polygon:
    points: list[Point]

    def __init__(self) -> None:
        self.points = []

    def __str__(self) -> str:
        return f'Polygon[{", ".join(str(point) for point in self.points)}]'

    def __getitem__(self, item: int | slice) -> Point | list[Point]:
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return self.points[item.start:item.stop:item.step]
        else:
            raise TypeError('Argument must be either integer or slice.')

    def add_point(self, point: Point) -> None:
        self.points.append(point)


print('ZADANIE 1')
p = Point()
print(f'X: {p.x}, Y: {p.y}')

print('\nZADANIE 2')
print(p)

print('\nZADANIE 3')
p.x, p.y = 2, 5
print(p)
print(p * 2)

print('\nZADANIE 4')
p_2 = Point(2, 5)
p_3 = Point(4, 10)
print(p == p_2)
print(p == p_3)

print('\nZADANIE 5')
poly = Polygon()
poly.add_point(p)
poly.add_point(p_2)
poly.add_point(p_3)
print(poly.points)

print('\nZADANIE 6')
print(poly)

print('\nZADANIE 7')
print(poly[2])
print(poly[:2])
print(poly[::2])
# print(poly['Raise Error'])
