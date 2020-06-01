# JTT feedback:
# Nice clear code and good descriptive variable names.

number = int(input("Enter a number"))

root = 1

while (root * root) < number:
    root = root + 1

divisor = 2
factor_found = False

while (factor_found == False) and (divisor <= root):
    r = number % divisor
    if r == 0:
        factor_found = True
    divisor = divisor + 1

if factor_found == False:
    print("Prime")
else:
    print("Not prime")


