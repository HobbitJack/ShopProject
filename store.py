from inventory_item import Item
from decimal import Decimal
from collections import namedtuple


class Shop:
    def __init__(self, inventory: dict[Item, tuple[Decimal, int]]):
        self.inventory = inventory
        self.cart: dict[Item, tuple[Decimal, int]] = {}

    def inventory_print(self):
        for item, metadata in self.inventory.items():
            print(f"{item}: {metadata}")
