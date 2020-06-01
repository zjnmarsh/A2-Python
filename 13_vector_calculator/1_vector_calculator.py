import math


class Vector:

    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    # def magnitude(self):
    #     squared = math.sqrt(self.x ** 2 + self.y ** 2)
    #     return squared

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # self.magnitude(x + y)
        return x, y, self.d

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return x, y

    def __rmul__(self,other):
        x = self.x * other
        y = self.y * other
        return x,y


    def __mul__(self, other):

        # scalar multiplication
        if (self.d == 'column' or self.d == 'row') and type(other) == int:
            x = self.x * other
            y = self.y * other
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



# v1 = v1.magnitude()
# print(v1)

v1 = Vector(6, 8, 'column')
v2 = Vector(3,4, 'row')
a = 3*v1

if matrix:
    print(str(a[0]) + '\n' + str(a[1]))
else:
    print(a)


# vector1 = Vector(3, 4, 'column')
# vector2 = Vector(2, -1, 'column')
# vector_addition = vector1 + vector2
# print(vector_addition)
# if vector_addition != (5, 3, 'column'):
#     print('fail addition!')
#
# vector3 = Vector(4, 2, 'column')
# vector_scalar_multiplication = vector3 * 3
# print(vector_scalar_multiplication)
# if vector_scalar_multiplication != (12, 6, 'column'):
#     print('fail scalar multiplication!')
#
# vector4 = Vector(7, 2, 'row')
# vector5 = Vector(3, 9, 'column')
# vector_rowcol_multiplication = vector4 * vector5
# print(vector_rowcol_multiplication)
# if vector_rowcol_multiplication != 39:
#     print('fail vector multiplication 1!')
#
# vector_colrow_multiplication = vector5 * vector4
# # I treat a 2x2 matrix as a column vector containing two row vectors
# if vector_colrow_multiplication != Vector( Vector(21,12,'row') , Vector(63,36,'row') , 'column' ):
#     print('fail vector multiplication 2!')
