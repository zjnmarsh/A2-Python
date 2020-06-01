def square(n):
    return n ** 2


def f(x):
    return (x) ** 2 + 10

def g(x):
    return (x) + 10


# print(addten(20))
# print(f(g()))


def maker(N):
    def action(X):
        return X * N

    return action


f = maker(2)
g = maker(3)

print(f'g(4) = {g(4)}')
print(f'f(2) = {f(2)}')
