class Car:

    def __init__(self, brand, colour, speed):
        self.brand  = brand
        self.colour = colour
        self.speed  = speed

    def describe(self):
        print(f'{self.brand} — {self.colour} — {self.speed} kmph')

c1 = Car('Toyota', 'Red',  120)
c2 = Car('Honda',  'Blue', 150)
c3 = Car('BMW',    'Black', 200)

c1.describe()
c2.describe()
c3.describe()

c1.colour = 'White'
c1.describe()

print(type(c1))
print(id(c1) == id(c2))
