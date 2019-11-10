from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling Card")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "you still have {} cards left".format(len(self.cards))


    def add_card(self, added_card):
        self.cards.extend(added_card)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has drawn {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0;

# Create New Deck and split in half
game = Deck()
game.shuffle()
half1, half2 = game.split_in_half()

# Create Both Players
comp = Player("Computer", Hand(half1))
name = input("What is your name? ")
human = Player(name, Hand(half2))

# Set Round Count
total_rounds = 0;
war_count = 0;

#Lets Play
while human.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round")
    print("here are the current standings")
    print(human.name + " still has " + str(len(human.hand.cards)))
    print(comp.name + " still has " + str(len(comp.hand.cards)))
    print("play a card")
    print("\n")

    # Cards on Table represented by list
    table_card = []

    # Play cards
    c_card = comp.play_card()
    h_card = human.play_card()

    # Add to table_cards
    table_card.append(c_card)
    table_card.append(h_card)

    # Check for War!
    if c_card[1] == h_card[1]:
        war_count+=1
        print("war")

        table_card.extend(human.remove_war_cards())
        table_card.extend(comp.remove_war_cards())

        c_card = comp.play_card()
        h_card = human.play_card()

        table_card.append(c_card)
        table_card.append(h_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(h_card[1]):
            human.hand.add_card(table_card)
        else:
            comp.hand.add_card(table_card)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(h_card[1]):
            human.hand.add_card(table_card)
        else:
            comp.hand.add_card(table_card)

print("game over, number of rounds " +str(total_rounds))











# print(half1)
# print(half2)

