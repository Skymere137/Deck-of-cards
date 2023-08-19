import random

# Create a list of suits and ranks to help define each card later
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# Create the card object to define the features of a single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
# Create the deck of cards by giving each card a rank and suit
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += str(card) + "\n"
        return deck_string

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __repr__(self):
        return self
    
    # Define a method for a game of Black Jack
    def black_jack():
        while True:
            counter = 0
            deck = Deck()
            deck.shuffle()

    # Deal two cards to the player and the dealer
            player_cards = {"card1": deck.deal_card(), "card2": deck.deal_card()}
            dealer_cards = {"card1": deck.deal_card(), "card2": deck.deal_card()}

    # Let player see his/her own cards but not dealer's
            print("Your Cards: ")
            for card in player_cards.values():
                
                print(f"{card.rank} of {card.suit}")
                
    # Set up a loop that gives the option to hit or stay     
            while True:
                counter += 1
                res = input("Hit or stay? \n> hit \n> stay \n> ")
                if res == "hit":
                    player_cards[f"card{counter}"] = deck.deal_card()
                    print(f"Your new card: {player_cards[f'card{counter}'].rank} of {player_cards[f'card{counter}'].suit}")
                else: 
                    break

            print("Dealer's Cards: ")
            for card in dealer_cards.values():
                
                print(f"{card.rank} of {card.suit}")

            
            inpt = input("Keep playing? \n> yes \n> no \n> ")
            if inpt == "yes":
                continue
            elif inpt == "no":
                break
            else: print("Sorry I didn't understand that!")