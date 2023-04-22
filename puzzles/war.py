

def draw_cards(n):
    for player in range(2):
        table[player] += cards[player][:n]              # draw player 1 cards to table
        del cards[player][:n]                           # remove them from deck

def battle():
    draw_cards(1)                                       # draw card players onto the table
    v = value[table[0][-1]]-value[table[1][-1]]         # value difference
    return 1 if v > 0 else 2 if v < 0 else -1           # determine winner

def move_cards(winner):
    global table                                        # get table from global scope
    cards[winner-1] += table[0] + table[1]              # move cards to winner's deck
    table = [[],[]]                                     # empty table
    return len(cards[0]) == 0 or len(cards[1]) == 0     # stops game if players have no more cars

def war():
    stop = False
    if len(cards[0]) < 4 or len(cards[1]) < 4:          # not enough cards to play war
        global game_winner                              # define global game winner
        game_winner = "PAT"                             # the players draw
        stop = True                                     # the game ends
    else:
        draw_cards(3)                                   # draw 3 cards from each player
        stop = play_round()                             # play another round
    return stop

def play_round():
    winner = battle()                                   # battle phase
    if winner > 0 :                                     # one of the player wins
        stop = move_cards(winner)
    else:                                               # draw
        stop = war()                                    # start war
    return stop

def find_winner():
    if game_winner != "":                               # the winner is already known (PAT)
        return game_winner
    else:
        n_cards = [len(deck) for deck in cards]         # number of cards in each deck
        #  wins the one with most cards (the other has zero)
        return f"{n_cards.index(max(n_cards))+1} {n_rounds}"

# globals

# value assigned to each card
value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
         "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 11,
         "Q" : 12, "K" : 13, "A" : 14}
cards = [[input()[:-1] for i in range(int(input()))],   # the n cards of player 1
         [input()[:-1] for i in range(int(input()))]]   # the m cards of player 2
table =  [[],[]]                                        # cards on the table

n_rounds = 0                                            # number of played rounds
game_winner = ""                                        # global game winner
stop = False                                            # trigger to end game

# game start

while stop == False:                                    # while game is not finished    
    stop = play_round()                                 # play next round
    n_rounds += 1                                       # increment number of rounds

print(find_winner())
