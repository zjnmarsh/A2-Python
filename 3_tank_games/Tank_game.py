
tankboard_player1 = [[' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ']]

tankboard_player2 = [[' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ']]

hitboard_player1 = [[' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ']]

hitboard_player2 = [[' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' '],
                     [' ',' ',' ',' ',' ',' ',' ']]






print("Player 1, put your tanks into locations! Enter coordinates in the format X,X, eg. 3,2 ")
for i in range(5):
    location = input("Enter coordinate for the tank.")
    tankboard_player1[int(location[0])][int(location[2])] = "T"

print("Player 2, put your tanks into locations! Enter coordinates in the format X,X, eg. 6,2")
for i in range(5):
    location = input("Enter coordinate for the tank")
    tankboard_player2[int(location[0])][int(location[2])] = "T"

x = 1
tanksleft_p1 = 0
tanksleft_p2 = 0


while x > 0:
    location = str(input("Player 1, enter a coordinate to destroy player 2's tank"))
    loc1 = int(location[0])
    loc2 = int(location[2])
    if tankboard_player2[loc1][loc2] == 'T':
        print("You hit a tank!")
        tanksleft_p2 = 0
        tankboard_player2[loc1][loc2] = ' '
        hitboard_player1[loc1][loc2] = 'H'
        for i in range(7):
            print(hitboard_player1[i])
        for i in range(7):
            for j in range(7):
                if tankboard_player2[i][j] == 'T':
                    tanksleft_p2 = tanksleft_p2 + 1
        if tanksleft_p2 == 0:
            print("Player 1 has won!")
            break
    else:
        hitboard_player1[loc1][loc2] = 'X'
        for i in range(7):
            print(hitboard_player1[i])

    location = str(input("Player 2, enter a coordinate to destroy player 1's tank"))
    loc1 = int(location[0])
    loc2 = int(location[2])
    if tankboard_player1[loc1][loc2] == 'T':
        print("You hit a tank!")
        tanksleft_p2 = 0
        tankboard_player1[loc1][loc2] = ' '
        hitboard_player2[loc1][loc2] = 'H'
        for i in range(7):
            print(hitboard_player2)
        for i in range(7):
            for j in range(7):
                if tankboard_player1[i][j] == 'T':
                    tanksleft_p1 = tanksleft_p1 + 1
        if tanksleft_p1 == 0:
            print("Player 2 has won!")
            break
    else:
        hitboard_player2[loc1][loc2] = 'X'
        for i in range(7):
            print(hitboard_player2[i])


"""
for i in range(7):
    print(tankboard_player1[i])

for i in range(7):
    print(tankboard_player2[i])
"""
