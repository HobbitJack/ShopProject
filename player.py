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

    def cleanup_inventory(self):
        """Cleanup this user's inventory

        Parameters:
            None

        Returns:
            None
        """
        if len(self.inventory) > 0:
            remove_list = []
            for item, amount in self.inventory.items():
                if amount == 0:
                    remove_list.append(item)
            for item in remove_list:
                self.inventory.pop(item)
