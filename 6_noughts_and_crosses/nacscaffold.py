board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
         ]

nowinner = True

"""
def wincheck():
    print("checking")
    for i in range(3):
        checklist = []
        checklist2 = []
        print("1")
        for j in range(3):
            print("2")
            checklist.append(board[i][j])
            checklist2.append(board[j][i])
        if checklist[0] == 'X' or checklist[0] == 'O':
            print("x or o")
            print(checklist)
            if checklist[0] == checklist[1] == checklist[2]:
                print("hello")

"""

checklist = []


def wincheck():
    for i in range(3):
        checklist = []
        checklist2 = []
        for j in range(3):
            checklist.append(board[i][j])
            checklist2.append(board[j][i])
        if checklist[0] == 'X' or checklist[0] == 'O':
            print("\n\n1st checklist search")
            print(checklist)
            print("\n\n")
            if checklist[0] == checklist[1] == checklist[2]:
                print("1st success")
                nowinner = False
        if checklist2[0] == 'X' or checklist2[0] == 'O':
            print("\n\n2nd checklist search")
            print(checklist2)
            print("\n\n")
            if checklist2[0] == checklist2[1] == checklist2[2]:
                print("2nd success")
                nowinner = False


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
    wincheck()




