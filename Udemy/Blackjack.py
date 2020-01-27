import random

class Card():
    def __init__(self,value,suit):
        self.suit = suit
        self.value = value
    def printcard(self):
        cardstr = ''
        if self.value == 1:
            cardstr += 'Ace'
        elif self.value == 11:
            cardstr += 'Jack'
        elif self.value == 12:
            cardstr += 'Queen'
        elif self.value == 13:
            cardstr += 'King'
        else:
            cardstr += str(self.value)
        cardstr += ' of '
        if self.suit == 1:
            cardstr += 'Clubs'
        elif self.suit == 2:
            cardstr += 'Diamonds'
        elif self.suit == 3:
            cardstr += 'Spades'
        else:
            cardstr += 'Hearts'
        print(cardstr)

class Deck():
    def __init__(self):
        self.cards = []
        for suit in range(1,5):
            for value in range(1,14):
                self.cards.append(Card(value, suit))
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)

class Hand():
    def __init__(self,deck):
        self.cards = []
        for i in range(2): self.cards.append(deck.cards.pop())
    def hit(self,deck):
        self.cards.append(deck.cards.pop())
    def score(self):
        total = 0
        numaces = 0
        for card in self.cards:
            if card.value == 1:
                numaces += 1
            if card.value == 1:
                total += 11
            elif card.value > 10:
                total += 10
            else:
                total += card.value
        while numaces > 0:
            if total > 21:
                total -= 10
                numaces -= 1
            else:
                break
        return total
    def printhand(self,player):
        if player == 'player':
            print("Your cards are:")
            for card in self.cards:
                card.printcard()
        if player == 'dealer':
            print("The dealer shows:")
            self.cards[0].printcard()

class purse():
    def __init__(self,buyin):
        self.cash = buyin
    def bid(self,amt):
        self.cash -= amt
    def payout(self,amt):
        self.cash += amt

def game():
    keep_playing = True
    player_purse = purse(100)
    while keep_playing:
        deck = Deck()
        while True:
            print("You have %d dollars." % (player_purse.cash))
            try:
                bid = int(input("How much would you like to bid? "))
            except:
                continue
            else:
                break
        bid_total = bid
        player_purse.bid(bid)
        player_hand = Hand(deck)
        dealer_hand = Hand(deck)
        dealer_hand.printhand('dealer')
        print('')
        player_hand.printhand('player')
        while True:
            hit = input("Would you like to hit? (y/n):")
            if hit == 'y':
                player_hand.hit(deck)
                player_hand.printhand('player')
            else:
                break
            if player_hand.score() > 21:
                break
        score = player_hand.score()
        if score > 21:
            print("Bust!")
        else:
            while dealer_hand.score() < score and dealer_hand.score() <= 21:
                dealer_hand.hit(deck)
            if score < dealer_hand.score() <= 21:
                print("The dealer wins with %d." % (dealer_hand.score()))
                print("Your score was %d." % (score))
            else:
                print("The dealer scored %d." % (dealer_hand.score()))
                print("Your score was %d." % (score))
                print("You win!")
                player_purse.payout(2*bid_total)
        if player_purse.cash < 0:
            print("You owe the casino money, so they break your thumbs.")
            break
        kp = input("Would you like to keep playing? (y/n):")
        if kp != 'y':
            keep_playing = False
    print("Your final score was %d" % (player_purse.cash))

game()