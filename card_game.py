"""

Challenge - Deck of Cards

Create 2 Classes:

Class Card

    Attributes:

        name
        value

Class Deck

    Attributes:

        pack: this should be initialised to a list of full deck of cards objects
        discarded: This should be initialised to an empty list

    Methods

        Shuffle
        Pick a card (should return a card instance from the top of the deck)

Create a simple higher or lower game using your deck of cards

"""

import random
from typing import List

class Card:
    all = [] # Stores all instances of this class "Card"
    def __init__(self, name: str, value: int):
        assert value >= 1 and value <= 13, "Card value should be between 1 and 13 only!"
        self.name = name
        self.value = value
        Card.all.append(self)

class Deck:
    def __init__(self, pack: List, discarded: List = []):
        self.original_pack = pack
        self.pack_names_only = [each.name for each in self.original_pack] 
        self.discarded = discarded

    def shuffle(self):

        # Creating randomess in the card order at first
        random.shuffle(self.pack_names_only)

        # Performing overhand shuffle 4 times
        for i in [(20, 45), (15, 40), (10,30), (30, 45)]:
            self.shuffing_deck = self.pack_names_only

            self.bottom_half_from_deck = self.shuffing_deck[:i[0]]
            self.block_of_cards_from_deck = self.shuffing_deck[i[0]:i[1]]
            self.top_half_from_deck = self.shuffing_deck[i[1]:]

            self.overhand_shuffled_deck = self.bottom_half_from_deck + self.top_half_from_deck + self.block_of_cards_from_deck
            self.pack_names_only = self.overhand_shuffled_deck
        
        #performing riffle shuffle once
        self.first_half_card_deck = self.pack_names_only[:len(self.pack_names_only)//2]
        self.second_half_card_deck = self.pack_names_only[len(self.pack_names_only)//2:]
        self.riffle_shuffled_deck = []
        for a, b in zip(self.first_half_card_deck, self.second_half_card_deck):
            self.riffle_shuffled_deck.append(a)
            self.riffle_shuffled_deck.append(b)
        self.pack_names_only = self.riffle_shuffled_deck
        
    def pick_a_card(self):
        self.top_card_name = self.pack_names_only.pop(-1)
        print(f"\nYou picked {self.top_card_name}. Remaining cards: {len(self.pack_names_only)}")

        for each in self.original_pack:
            if each.name == self.top_card_name:
                self.top_card_value = each.value

        return self.top_card_name, self.top_card_value

def main():
    all_card_numbers = [x for x in range(1,14)]
    all_cards_names = [
        "Ace", 
        "Two", 
        "Three", 
        "Four", 
        "Five", 
        "Six", 
        "Seven", 
        "Eight", 
        "Nine", 
        "Ten", 
        "Jack", 
        "Queen", 
        "King"
    ]
    card_suits = [
        "spades", 
        "hearts", 
        "diamonds", 
        "clubs"
    ]

    for card_name, card_number in zip(all_cards_names, all_card_numbers):
        for card_suit in card_suits:
            # print(f"{card_name} of {card_suit}: {card_number}")
            card_full_name = f"{card_name} of {card_suit}"
            locals()[card_full_name] = Card(card_full_name, card_number)

    all_cards_objects_in_a_list = Card.all

    a_new_deck_of_card = Deck(all_cards_objects_in_a_list, [])

    a_new_deck_of_card.shuffle() #Shuffling once

    player1_card = a_new_deck_of_card.pick_a_card() # Retreving the top card

    player2_card = a_new_deck_of_card.pick_a_card() # Retreving the top card

if __name__ == "__main__":
    main()