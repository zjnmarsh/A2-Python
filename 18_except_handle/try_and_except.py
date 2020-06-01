usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("You have not entered a valid number")
        raise
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        print("Your number is either too high or too low")
    try:
        division = 301 / number
        print(f"301 divided by {number} = {division}")
    except ZeroDivisionError:
        print("You cannot divide by zero")


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)
