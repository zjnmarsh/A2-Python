usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']
numbers = [0,1,2,3,4,5,6,7,8,9]

def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    if usernumber != int(usernumber):
        print("You entered an invalid number, using 1 instead")
        usernumber = 1
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    if number == 0:
        print("You cannot divide by 0, dividing by 1 instead")
        number = 1
    division = 301 / number
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)

