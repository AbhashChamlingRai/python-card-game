import random

class Deck:

    def __init__(self, pack: list, discarded = []):
        self.__original_pack = pack
        self.__discarded = discarded

    def set_pack(self, new_pack: list):
        self.__original_pack = new_pack

    def shuffle(self):

        # Creating randomess in the card order at first
        random.shuffle(self.__original_pack)

        # Performing overhand shuffle 4 times
        for i in [(20, 45), (15, 40), (10,30), (30, 45)]:
            self.shuffing_deck = self.__original_pack

            self.middle_part_of_deck = self.shuffing_deck[:i[0]]
            self.middle_part_of_deck = self.shuffing_deck[i[0]:i[1]]
            self.top_part_of_deck = self.shuffing_deck[i[1]:]

            # When overhand shuffling middle part goes top!
            self.overhand_shuffled_deck = self.middle_part_of_deck + self.top_part_of_deck + self.middle_part_of_deck

            # Setting the pack
            self.set_pack(self.overhand_shuffled_deck)
        
        #performing riffle shuffle once
        self.first_half_of_deck = self.__original_pack[:len(self.__original_pack)//2]
        self.second_half_of_deck = self.__original_pack[len(self.__original_pack)//2:]
        self.riffle_shuffled_deck = []
        for a, b in zip(self.first_half_of_deck, self.second_half_of_deck):
            self.riffle_shuffled_deck.append(a)
            self.riffle_shuffled_deck.append(b)

        # Setting the pack
        self.set_pack(self.riffle_shuffled_deck)
        
    def pick_a_card(self):
        self.top_card = self.__original_pack.pop(-1)
        print(f"\nYou picked {self.top_card.get_card_name()}. Remaining cards: {len(self.__original_pack)}")

        return self.top_card.get_card_name(), self.top_card.get_card_value()