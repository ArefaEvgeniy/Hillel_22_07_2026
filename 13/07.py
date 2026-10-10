class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_from_origin(self):
        return ((self.x ** 2 + self.y ** 2) ** 0.5)


point_1 = Point(3, 4)
point_2 = Point(7, 0)
point_3 = Point(3, 4)
point_4 = Point(3, 3)

print(point_1.distance_from_origin())
print(point_2.distance_from_origin())

print(point_1)
print(point_2)

print(point_1 == point_3)
print(point_1 == point_4)
