class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, point2) -> bool:
        return self.x == point2.x and self.y == point2.y

    def __gt__(self, point2):
        return self.x > point2.x and self.y > point2.y


point = Point(2, 3)
point2 = Point(1, 2)
print(point > point2)
