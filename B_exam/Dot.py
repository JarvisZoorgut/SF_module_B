class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x, self.y}'

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * (self.r ** 2)

c_1 = Circle(5)
c_2 = Circle(10)

print(Circle.get_area(c_1))
print(Circle.get_area(c_2))


p1 = Dot(1, 2)
p2 = Dot(2, 2)
print(p1 == p2)
print(str(p1))
print(p2)