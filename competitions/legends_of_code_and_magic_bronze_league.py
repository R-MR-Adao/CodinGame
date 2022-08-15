import sys
import math

sys.setrecursionlimit(20000)

def printf(s)
    print(s, file=sys.stderr, flush=True)

class Card()
    def __init__(self,instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change)
        self.instance_id = instance_id
        self.location = location
        self.card_type = card_type
        self.cost = cost
        self.attack = attack
        self.defense = defense
        self.abilities = {'C'False, 'B'False,'G'False,'-'True}
        for c in abilities self.abilities[c] = c != '-'
        self.my_health_change = my_health_change
        self.opponent_health_change = opponent_health_change
    
    def par(self, par) # outputs the requested card parameter
        return eval(self.+par)

    def format(self)# outputs a single card as formatted string
        return str(self.instance_id)

class DeckIterator()
   def __init__(self, deck)
        self._deck = deck    # Team object reference
        self._index = -1     # member variable to keep track of current index

   def __next__(self)
        if self._index  (len(self._deck)-1)
            self._index +=1
            return self._deck[self._index]
        else # End of Iteration
            raise StopIteration

class Deck()
    def __init__(self)
        self.cards = []     # list of cards in deck
    
    def addNewCard(self,instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change)
        self.cards.append(Card(instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change))
    
    def addCard(self, card)
        self.cards.append(card)

    def removeCard(self,card)
        del self.cards[self.cards.index(card)]
    
    def mostParameter(self, fun, par) # find most valued parameter
        l = [c.par(par) for i,c in enumerate(self.cards)]
        v = fun(l)
        return v, self.cards[l.index(v)], l.index(v)
    
    def summonable(self, mana) # returns a list of summonable cards
        return [c for c in self.cards if c.cost  mana]
    
    def __iter__(self)
       ''' Returns the Iterator object '''
       return DeckIterator(self)

    def __len__(self)
        return len(self.cards)

    def __getitem__(self, item)
        return self.cards[item]
    
    def hand(self) # returns the list of cards in hand
        return [c for c in self.cards if c.location == 0]

    def board(self) # returns the list of cards in board
        return [c for c in self.cards if c.location == 1]
    
    def opponent(self) # return the list of cards in opponent
        return [c for c in self.cards if c.location == -1]

class Player()
    def __init__(self, health, mana, deck_n, rune, draw)
        self.health = health
        self.mana = mana
        self.Deck_n = deck_n
        self.rune = rune
        self.card_draw = draw
        self.board = Deck()
        self.hand = Deck()
        self.actions = {}  # list of actions in previous round (reserved for opponent)
    
    def setHandActions(self, hand_n, actions_n)
        self.hand_n = hand_n
        self.actions_n = actions_n
    
    def setActions(self, card_number, actions)
        self.actions[card_number] = actions

def draft_getMostParmeter_array(ables,fun, par)
    d = [card.par(par) for card,i in ables.items()]
    ind = [i for card,i in ables.items()]
    return ind[d.index(fun(d))]                                        # max defense
def checkIfCharger(card, deck)
    if card.abilities['C'] # cqrd has the Charge hability
        deck.board.addCard(card)

def getMostParmeter_array(card_array, fun, par)
    card_par = [card.par(par) for card in card_array]
    return card_array[card_par.index(fun(card_par))]

def checkIfBreakthrough(card, card_array, guards)
    if card.abilities['B'] # card has the breakthrough hability
        if guards          # guards in opponent board
            opp = getMostParmeter_array(card_array, min, defense)
        else
            opp = '-1'
    else
        opp = getMostParmeter_array(card_array, max, attack)
    return opp

def useItem(card)
    s = 'USE ' + card.format() + ' '
    if card.card_type == 1      # Green item
        if len(my.board)  0
            if card.attack  card.defense
                myCard = my.board.mostParameter(max,'defense')[1]
                s += myCard.format()
            else
                myCard = my.board.mostParameter(max,'attack')[1]
                s += myCard.format()
            myCard.attack += card.attack
            myCard.defense += card.defense
            s +=  ;
        else
            s = 'nope'
    elif card.card_type == 2    # Red item
        if len(opponent.board)  0
            if abs(card.attack)  abs(card.defense)
                oppCard = opponent.board.mostParameter(max,'attack')[1]
                s += oppCard.format()
            else
                oppCard = opponent.board.mostParameter(min,'defense')[1]
                s += oppCard.format()
            oppCard.attack += card.attack
            oppCard.defense += card.defense
            s +=  ;
        else
            s = 'nope'
    elif card.card_type == 3    # Blue item
        if card.defense  0 # deal damage to creature
            if len(opponent.board)  0
                oppCard = opponent.board.mostParameter(max,'defense')[1]
                s += oppCard.format()
                oppCard.attack += card.attack
                oppCard.defense += card.defense
                s +=  ;
            else
                s = 'nope'
        else
            s += '-1;'
    else
        s = ''
    return s

def summonSequence()
    nope = False                                                # flag invaid use of item
    my_hand_min_cost = my.hand.mostParameter(min, 'cost')[1]
    if my_hand_min_cost.card_type  0                          # item
        s = useItem(my_hand_min_cost) 
        if s == 'nope'                                         # cannot use card
            nope = True
            my.hand.removeCard(my_hand_min_cost)
            my_hand_min_cost = my.hand.mostParameter(min, 'cost')[1]
    if nope and my_hand_min_cost.card_type  0                          # item
        s = summonSequence()                                    # Recursively try to find a creature or a suitable item
    elif my_hand_min_cost.card_type == 0                                                       # Creature
        s = 'SUMMON ' + my_hand_min_cost.format() + ';'
        printf(No cards Summon)
        my.hand.removeCard(my_hand_min_cost)
        checkIfCharger(my_hand_min_cost, my)     # move card if it has the Charge ability
    return s

def stratTwo()
    manaThreshold = 10                          # threshold to decide on mana economy mode
        # Always summon the card with maximun health and atack player with max power
    s = ''
    if len(my.board.cards) == 0
        for i in range(my.card_draw)
            s = summonSequence()
            if s == nope
                s = ''
            else
                 my.card_draw -= 1
                
    if len(my.board.cards)  0
        cardsSum = my.hand.summonable(my.mana)
        ii = 0
        #for i in range(my.card_draw)                    # try to summon new card
        while ii  my.card_draw
            if len(cardsSum)  0
                items = [card for card in cardsSum if card.card_type 0]
                printf(Try to summon new card)
                if len(my.board)  len(opponent.board)
                    guards = [card for card in cardsSum if card.abilities['G']]
                    if len(guards)  0 and ii  1
                        if my.mana  manaThreshold
                            card_draw = getMostParmeter_array(guards, min, cost)
                        else
                            card_draw = getMostParmeter_array(guards, max, cost)
                    else
                        if len(items)  0
                            if my.mana  manaThreshold
                                card_draw = getMostParmeter_array(items, min, 'cost')
                            else
                                card_draw = getMostParmeter_array(items, max, 'cost')
                        else
                            card_draw = getMostParmeter_array(cardsSum, max, 'attack')
                else
                    card_draw = getMostParmeter_array(cardsSum, max, 'defense')
                if card_draw.card_type == 0                  # creature    
                    s += 'SUMMON ' +    card_draw.format() + ';'
                else                                    # item
                    s = useItem(card_draw)
                    if s[-4] == 'nope'
                        my.card_draw += 1
                        s = s[0-4]
                my.mana -= card_draw.cost
                my.hand.removeCard(card_draw)            # remove from hand
                checkIfCharger(card_draw, my)            # move card if it has the Charge ability
                cardsSum = my.hand.summonable(my.mana)   # update summable cards
            ii += 1
        # start attacking sequence
        for i in range(len(my.board.cards))
            card = my.board.cards[i]
            opp_guards = [card for card in opponent.board if card.abilities['G']]
            if len(opp_guards)  0
                opp = checkIfBreakthrough(card, opp_guards, True)
            else
                if (i = len(opponent.board.cards))
                    opp = '-1'
                else
                    opp_breaks = [card for card in opponent.board if card.abilities['B']]
                    if len(opp_breaks)  0
                        opp = checkIfBreakthrough(card, opp_breaks, False)
                    else    
                        opp = checkIfBreakthrough(card, opponent.board.cards, False)
                    if (type(opp) == type(card) and card.abilities['G'] and card.attack  opp.defense) # prevent guard waste
                        opp = '-1'                                          # force invalid
            if type(opp) == type(card)
                if card.attack = opp.defense
                    opponent.board.removeCard(opp)
                opp.defense -= card.attack
            s += 'ATTACK ' + card.format() + ' ' + opp.format() + ';'
    return s

def stratThree()
    manaThreshold = 10                          # threshold to decide on mana economy mode
        # Always summon the card with maximun health and atack player with max power
    s = ''
    if len(my.board.cards) == 0
        for i in range(my.card_draw)
            s = summonSequence()
            if s == nope
                s = ''
            else
                 pass#my.card_draw -= 1
                
    if len(my.board.cards)  0
        cardsSum = my.hand.summonable(my.mana)
        ii = 0
        #for i in range(my.card_draw)                    # try to summon new card
        while ii  my.card_draw
            if len(cardsSum)  0
                items = [card for card in cardsSum if card.card_type 0]
                printf(Try to summon new card)
                if len(my.board)  len(opponent.board)
                    guards = [card for card in cardsSum if card.abilities['G']]
                    if len(guards)  0 and ii  1
                        if my.mana  manaThreshold
                            card_draw = getMostParmeter_array(guards, min, cost)
                        else
                            card_draw = getMostParmeter_array(guards, max, cost)
                    else
                        if len(items)  0
                            if my.mana  manaThreshold
                                card_draw = getMostParmeter_array(items, min, 'cost')
                            else
                                card_draw = getMostParmeter_array(items, max, 'cost')
                        else
                            card_draw = getMostParmeter_array(cardsSum, max, 'attack')
                else
                    card_draw = getMostParmeter_array(cardsSum, max, 'defense')
                if card_draw.card_type == 0                  # creature    
                    s += 'SUMMON ' +    card_draw.format() + ';'
                else                                    # item
                    s = useItem(card_draw)
                    if s[-4] == 'nope'
                        my.card_draw += 1
                        s = s[0-4]
                my.mana -= card_draw.cost
                my.hand.removeCard(card_draw)            # remove from hand
                checkIfCharger(card_draw, my)            # move card if it has the Charge ability
                cardsSum = my.hand.summonable(my.mana)   # update summable cards
            ii += 1
        # start attacking sequence
        for i in range(len(my.board.cards))
            card = my.board.cards[i]
            opp_guards = [card for card in opponent.board if card.abilities['G']]
            if len(opp_guards)  0
                opp = checkIfBreakthrough(card, opp_guards, True)
            else
                if (i = len(opponent.board.cards))
                    opp = '-1'
                else
                    if card.abilities['G']
                        opp_weak = [oppCard for oppCard in opponent.board if card.attack = oppCard.defense]
                        if len(opp_weak)  0
                            opp = checkIfBreakthrough(card, opp_weak, False)
                        else
                            opp = '-1'
                    else
                        opp_breaks = [card for card in opponent.board if card.abilities['B']]
                        if len(opp_breaks)  0
                            opp = checkIfBreakthrough(card, opp_breaks, False)
                        else    
                            opp = checkIfBreakthrough(card, opponent.board.cards, False)
            if type(opp) == type(card)
                if card.attack = opp.defense
                    opponent.board.removeCard(opp)
                opp.defense -= card.attack
            s += 'ATTACK ' + card.format() + ' ' + opp.format() + ';'
    return s

phase = 'draft'     # game phase
nPlay = 0           # play number
nBattle = 0         # battle plays number
print(Draft phase, file=sys.stderr, flush=True)
while True
    nPlay += 1
    
    player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
    my = Player(player_health, player_mana, player_deck, player_rune, player_draw)
    printf(Player draw = {}.format(player_draw))

    player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
    opponent = Player(player_health, player_mana, player_deck, player_rune, player_draw)
    opponent_hand, opponent_actions = [int(i) for i in input().split()]
    opponent.setHandActions(opponent_hand, opponent_actions)
    for i in range(opponent_actions)
        s = input().split()
        if len(s)  0
            #card_number, action, cardId = s.split()
            opponent.setActions(s[0], s[1])
    
    card_count = int(input())
    for i in range(card_count)
        inputs = input().split()
        card_number =            int(inputs[0])
        instance_id =            int(inputs[1])
        location =               int(inputs[2])
        card_type =              int(inputs[3])
        cost =                   int(inputs[4])
        attack =                 int(inputs[5])
        defense =                int(inputs[6])
        abilities =              inputs[7]
        my_health_change =       int(inputs[8])
        opponent_health_change = int(inputs[9])
        card_draw =              int(inputs[10])
        
        if location == 0
            my.hand.addNewCard(instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change)
        elif location == 1
            my.board.addNewCard(instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change)
        else opponent.board.addNewCard(instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change)

    if phase == 'draft'
        v, c, i = my.hand.mostParameter(max,'defense')
        # override decision if chargers are available
        guards   = {cardi for i,card in enumerate(my.hand) if card.abilities['G']} # search guards
        items    = {cardi for i,card in enumerate(my.hand) if card.card_type  0}  # search items
        if len(items)  0
            i = draft_getMostParmeter_array(items,min, 'cost')
        if len(guards)  0
            i = draft_getMostParmeter_array(guards,min, 'cost')
        print('PICK '+str(i))
        if nPlay = 30         # change game phase
            phase = 'battle'
            print(Battle phase, file=sys.stderr, flush=True)
    else
        nBattle += 1
        printf(My hand = {}.format([c.instance_id for c in my.hand]))
        printf(My board = {}.format([c.instance_id for c in my.board]))
        printf(Opponent board = {}.format([c.instance_id for c in opponent.board]))
        
        s = stratThree()
        print(s)
    
    #print(Debug messages..., file=sys.stderr, flush=True)