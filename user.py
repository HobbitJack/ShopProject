"""Module for a simple player"""
import item as it


class User:
    """Stand-in Player class

    Attributes:
        wallet: float = The amount of money the user has
        inventory: dict[it.Item, int] = The user's inventory

    Methods:
        print_inventory() -> None: Print the user's inventory and clear non-present items
    """

    def __init__(self, wallet: int):
        self.wallet: float = wallet
        self.inventory: dict[it.Item, int] = {}

    def print_inventory(self) -> None:
        """Print the user's inventory and clear non-present items

        Parameters:
            None

        Returns:
            Nothing
        """
        print(f"Wallet: ${self.wallet:.2f}")
        if len(self.inventory) > 0:
            remove_list = []
            for item, amount in self.inventory.items():
                if amount == 0:
                    remove_list.append(item)
            for item in remove_list:
                self.inventory.pop(item)

            if len(self.inventory) > 0:
                for item, amount in self.inventory.items():
                    if item.durability == -1:
                        print(f"{item.name}: {amount}")
                    else:
                        print(f"{item.name}: {amount}, {item.durability}%")
            else:
                print("Inventory is empty.")
        else:
            print("Inventory is empty.")
