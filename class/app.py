class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"drawing point ({self.x} , {self.y})")

    @classmethod
    def factory(cls):
        return cls(2, 3)

    def __str__(self):
        return f"({self.x}, {self.y})"


point = Point.factory()
#point = Point(1, 2)
print(point)

point.draw()

# class attributes
print(Point.default_color)

isinstance(point, Point)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if(price) < 0:
            raise ValueError("Price can not be negative")
        self.__price = price


product = Product(2)
product.price = 20
