import math

class Shape:
    def area(self):
        # base version — overridden by children
        return 0

    def describe(self):
        print(f'This shape has area: {self.area():.2f}')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):    # OVERRIDE
        # return math.pi * radius^2
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):    # OVERRIDE
        # return width * height
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):    # OVERRIDE
        # return 0.5 * base * height
        return 0.5 * self.base * self.height


# POLYMORPHISM — same method call, different result:
shapes = [Circle(7), Rectangle(5, 10), Triangle(6, 8)]
for shape in shapes:
    shape.describe()   # each calls its own area()

# Expected output:
# This shape has area: 153.94
# This shape has area: 50.00
# This shape has area: 24.00
