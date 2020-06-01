def whole_to_bin(w):
    bin = ''
    while w > 0:
        bin = str(w % 2) + bin
        w = w // 2
    return bin


def frac_to_bin(f):
    bin = ''
    orig_f = f
    allocatedFractionalNoOfBits = 3
    while True:
        r = f * 2
        print(f'frac x 2 : {r}')
        bin = bin + str(r)[0]
        f = r - int(r)
        print(f'remainder : {f}')
        if f == 0 or f == orig_f or len(bin) > allocatedFractionalNoOfBits:
            break
    return bin


def fixed_to_bin(number):
    whole = int(number)
    decimal = number - whole

    whole_bin = whole_to_bin(whole)
    decimal_bin = frac_to_bin(decimal)

    full_decimal = whole_bin + '.' + decimal_bin

    return full_decimal


# print(frac_to_bin(0.75))

# does not work when no allocatedFractionalNoOfBits
# print(frac_to_bin(0.8))

print(fixed_to_bin(2.75))
