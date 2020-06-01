import random

playing_deck = [[],[]]
player_decks = []
player_games = []
total = 0


def new_deck():
    global playing_deck
    suits = ['Hearts','Spades','Clubs','Diamonds']
    card_types = ['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']
    card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    playing_deck = []

    for cards in suits:
        for types in card_types:
            new_card = types + ' Of ' + cards
            value = card_values[card_types.index(types)]
            playing_deck.append([new_card, value])

    for i in range(len(playing_deck)):
        rand = random.randint(0,i)
        playing_deck[i], playing_deck[rand] = playing_deck[rand], playing_deck[i]


def no_players():
    global playing_deck, player_decks, player_games
    players = int(input("How many players are there"))
    return players

def first_deal():
    players = no_players()
    for i in range(players):
        for j in range(2):
            x = playing_deck.pop()
            print(x)
            player_decks[[i][j]] = x

new_deck()
first_deal()
