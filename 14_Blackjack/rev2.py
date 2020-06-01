import random

suits = []
card_types = []
card_values = []
playing_deck = []
p1_deck = []
p2_deck = []
p1_games = 0
p2_games = 0
total = 0


def preparation():
    global suits, card_types, card_values, playing_deck, p1_deck, p2_deck, p1_games, p2_games, total


    suits = ['Hearts','Spades','Clubs','Diamonds']
    card_types = ['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']
    card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    playing_deck = []
    p1_deck = []
    p2_deck = []
    p1_games = 0
    p2_games = 0
    total = 0

    # prepares and shuffles the card deck
    for cards in suits:
        for types in card_types:
            new_card = types + ' Of ' + cards
            value = card_values[card_types.index(types)]
            playing_deck.append([new_card, value])

    for i in range(len(playing_deck)):
        rand = random.randint(0,i)
        playing_deck[i], playing_deck[rand] = playing_deck[rand], playing_deck[i]

def linebreak():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def deal(deck):
    for i in range(2):
        deck.append(playing_deck.pop())
    return deck

def twist(deck):
    deck.append(playing_deck.pop())
    return deck

def value_total(deck):
    total = 0
    for i in range(len(deck)):
        total = total + int(deck[i][1])
    return total

def check_21(deck,x):
    score = value_total(deck)
    if score > 21:
        print("Your cards are", deck)
        print("Your total is over 21! You're bust!")
        for j in range(len(deck)):
            deck.pop()
    else:
        print("Your cards are", deck)
        print("Your current total is", score)
        x = 1
        return x

def ask_player(deck):
    x = 0
    check = check_21(deck, x)
    if check == 1:
        usr_in = input("Would you like to twist a card? y or n ")
        if usr_in == 'y':
            twist(deck)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            check_21(deck,1)




def gameplay():
        global p1_games
        global p2_games

        deal(p1_deck)
        deal(p2_deck)

        ask_player(p1_deck)
        x = input("Press enter to finish turn")
        print("***********************************************************")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        ask_player(p2_deck)
        x = input("Press enter to finish turn")
        print("***********************************************************")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        p1_score = value_total(p1_deck)
        p2_score = value_total(p2_deck)

        if p1_score > p2_score:
            print("Player 1 is the winner!!")
            p1_games += 1
        elif p2_score > p1_score:
            print("Player 2 is the winner!!")
        else:
            print("This must be a draw! ")


def menu():
    x = True
    while x is True:
        preparation()
        gameplay()
        k = input("Do you want to play another round? y or n ")
        if k == 'n':
            if p1_games > p2_games:
                print("Player 1 is the winner with ", p1_games, " games!!")
            elif p2_games > p1_games:
                print("Player 2 is the winner with ", p2_games, " games!!")
            else:
                print("This must be a draw :( ")
            x = False
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


menu()

