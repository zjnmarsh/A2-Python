import math


class Vector:

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def magnitude(self):
        squared = math.sqrt(self.x ** 2 + self.y ** 2)
        return squared

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        self.magnitude(x + y)
        return x, y, self.d

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return x, y

    def __mul__(self, other):

        # scalar multiplication
        if (self.d == 'column' or self.d == 'row') and type(other) == int:
            x = other * self.x
            y = other * self.y
            return x, y, self.d

        # row and column multiplication
        elif self.d == 'row' and other.d == 'column':
            x = self.x * other.x
            y = self.y * other.y
            ans = x + y
            return ans

        # standard vector
        elif (self.d == 'row' and other.d == 'row') or (self.d == 'column' and other.d == 'column'):
            x = self.x * other.x
            y = self.y * other.y
            return x, y

        # returns a matrix
        elif self.d == 'column' and other.d == 'row':
            top = []
            bottom = []
            top.append(self.x * other.x)
            top.append(self.x * other.y)
            bottom.append(self.y * other.x)
            bottom.append(self.y * other.x)
            global matrix
            matrix = True
            return top, bottom


matrix = False

# --------------------------------------------------------------------------

=






v1 = v1.magnitude()
print(v1)

v1 = Vector(6, 8, 'column')
v2 = Vector(3,4, 'row')
a = v1 * v2

if matrix:
    print(str(a[0]) + '\n' + str(a[1]))
else:
    print(a)
