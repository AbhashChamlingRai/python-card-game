class Card:

    __all_cards_objects = [] # Stores all instances of this class "Card"

    def __init__(self, name: str, value: int):
        assert value >= 1 and value <= 13, "Card value should be between 1 and 13 only!"
        self.__name = name
        self.__value = value
        Card.__all_cards_objects.append(self)

    def get_card_name(self):
        return self.__name
    def set_card_name(self, new_name):
        self.__name = new_name

    def get_card_value(self):
        return self.__value
    def set_card_value(self, new_value):
        self.__name = new_value

    @classmethod
    def get_all_cards_objects(cls):
        return cls.__all_cards_objects