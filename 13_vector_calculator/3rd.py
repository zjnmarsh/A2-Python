import math

class Vector:

    def __init__(self, vector, direction):
        self.vector = vector
        self.d = direction

    def __add__(self, other):
        for i in range(len(self.vector)):
            final_vector.append(self.vector[i] + other.vector[i])
        return final_vector

    def __sub__(self, other):
        for i in range(len(self.vector)):
            final_vector.append(self.vector[i] - other.vector[i])
        return final_vector

    def __rmul__(self, other):
        for i in range(len(self.vector)):
            final_vector.append(self.vector[i] * other)
        return final_vector

    def __mul__(self, other):

        # scalar multiplication
        if (self.d == 'column' or self.d == 'row') and type(other) == int:
            for i in range(len(self.vector)):
                final_vector.append(self.vector[i] * other)
            return final_vector

        # row and column multiplication
        elif self.d == 'row' and other.d == 'column':
            for i in range(len(self.vector)):
                final_vector.append(self.vector[i] * other.vector[i])
                ans = 0
                for number in final_vector:
                    ans += number
            return ans

        # standard vector
        elif (self.d == 'row' and other.d == 'row') or (self.d == 'column' and other.d == 'column'):
            for i in range(len(self.vector)):
                final_vector.append(self.vector[i] * other.vector[i])
            return final_vector

        # returning a matrix
        elif self.d == 'column' and other.d == 'row':
            final = []
            for i in range(len(self.vector)):
                for j in range(len(other.vector)):
                    final.append(self.vector[i] * other.vector[j])
            return final

    # def __str__(self):
    #       return v1

    def magnitude(self,other):
        return math.sqrt(self.vector**2 + other.vector**2)

v1 = Vector([2,7,6], "column")
v2 = Vector([2,3,4], "row")
final_vector = []

v3 = v1 * v2

print(v3)
Vector.magnitude(v1)
m
