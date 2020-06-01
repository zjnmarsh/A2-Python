# JTT feedback:
# Looks great so far; still a few debugging print()s in use, and your row/column indexing is 0-based (a human user might prefer 1-based), but it works nicely.

board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']
         ]


nowinner = True

"""
check = []
def wincheck():
    for i in range(3):
        for j in range(3):
            check[i][j] = board[i][j]
    if check[0] == check[1] == check[2]:
        nowinner == False
        print("Player", check[0], "has won!!")
"""

checklist = []

def wincheck():
    print("checking")
    for i in range(3):
        print("1")
        for j in range(3):
            print("2")
            checklist.append(board[i][j])
        if checklist[0] == checklist[1] == checklist[2]:
            print("hello")








while nowinner == True:
    for i in range(3):
        print(board[i])
    coordinate = str(input("Enter coordinate for X eg. z,z"))
    x_coord = coordinate[2]
    y_coord = coordinate[0]
    board[int(x_coord)][int(y_coord)] = 'X'
    wincheck()


    for i in range(3):
        print(board[i])

    coordinate = str(input("Enter coordinate for O eg. z,z"))
    x_coord = coordinate[2]
    y_coord = coordinate[0]
    board[int(x_coord)][int(y_coord)] = 'O'




