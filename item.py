"""Stand-in Item module"""


class Item:
    """Stand-in Item class

    Atrributes:
        self.name: str = The item's name
        self.durability = The item's percent durability

    Methods:
        None
    """

    def __init__(self, name: str, durability=-1):
        self.name = name
        self.durability = durability
