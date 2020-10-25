import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalized(self):
        magnitude = self.magnitude()
        return Vector2(self.x / magnitude, self.y / magnitude)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def translate(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y

    def array(self):
        return [self.x, self.y]

    def tuple(self):
        return tuple(self.array())

    def __eq__(self, other):
        return  self.x == other.x and  self.y == other.y

up = Vector2(0, 1)
down = Vector2(0, -1)
left = Vector2(-1, 0)
right = Vector2(1, 0)
zero = Vector2(0, 0)
one = Vector2(1, 1)