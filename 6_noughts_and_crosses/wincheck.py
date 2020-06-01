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
        if checklist2[0] == 'X' or checklist2[0] == 'O':
            print("\n\n2nd checklist search")
            print(checklist2)
            print("\n\n")
            if checklist2[0] == checklist2[1] == checklist2[2]:
                print("2nd success")
