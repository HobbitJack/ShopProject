"""Module for a simple player"""
from dataclasses import dataclass
import decimal
import inventory_item as it


@dataclass
class Player:
    """Stand-in Player class

    Dataclass
    Attributes:
        wallet: float = The amount of money the user has
        inventory: dict[it.Item, int] = The user's inventory
    """

    wallet: decimal.Decimal
    inventory: dict[it.Item, int]
