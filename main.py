from card import Card
from deck import Deck

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

            card_object_name = card_full_name.replace(" ", "_")
            locals()[card_object_name] = Card(card_full_name, card_number)

    all_cards_objects_in_a_list = Card.get_all_cards_objects()

    a_new_deck_of_card = Deck(all_cards_objects_in_a_list, [])

    a_new_deck_of_card.shuffle() #Shuffling once

    player1_card = a_new_deck_of_card.pick_a_card() # Retreving the top card
    print(player1_card)

    player2_card = a_new_deck_of_card.pick_a_card() # Retreving the top card
    print(player2_card)

if __name__ == "__main__":
    main()