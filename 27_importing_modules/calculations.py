def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


print('inside calculations.py')
print(f'__name__ = {__name__}')
if __name__ == "__main__":
    print(f'5 + 6 = {add(5, 6)}')
    print(f'5 x 6 = {multiply(5, 6)}')
