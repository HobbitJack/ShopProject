"""Stand-in Item module"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Stand-in Item class
    Dataclass

    Atrributes:
        self.name: str = The item's name
        self.durability = The item's percent durability

    Methods:
        None
    """

    name: str
    durability: float
