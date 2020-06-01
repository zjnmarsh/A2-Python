user_number = int(input("What would you like to go up to?"))

numberlist = []
for i in range(user_number):
    numberlist.append(i)
numberlist.append(user_number)
numberlist.remove(0)
numberlist.remove(1)

def delete_nonprime(p):
    for i in range(len(numberlist)):
        if numberlist[i] % p == 0 and numberlist[i] / p > 1:
            numberlist[i] = -3

delete_nonprime(2)
delete_nonprime(3)
delete_nonprime(5)
delete_nonprime(7)

for i in range(numberlist.count(-3)):
    numberlist.remove(-3)

print("The prime numbers are: ")
print(numberlist)
