"""This module implements our Shop and its logic."""
from decimal import Decimal
from typing import TypeVar, Generic, Protocol


class ItemHasAttributes(Protocol):
    """This class ensures the ItemClass TypeVar also checks for our necessary properties"""

    name: str


ItemClass = TypeVar("ItemClass", bound=ItemHasAttributes)


class PlayerHasAttributes(Generic[ItemClass], Protocol):
    """This class ensures the PlayerClass TypeVar also checks for our necessary properties"""

    wallet: Decimal
    inventory: dict[ItemClass, int]


PlayerClass = TypeVar("PlayerClass", bound=PlayerHasAttributes)


class Shop(Generic[ItemClass, PlayerClass]):
    """This class is our primary implementation of the Shop.
    Importing and using this should:tm: work.

    Inherits From:
        typing.Generic

    Attributes:
        self.inventory: dict[ItemClass, tuple[Decimal, int]] = Stores the item, price,
            and amount for this store's stock
        self.cart: dict[ItemClass, tuple[Decimal, int]] = Stores the item, price,
            and amount for items in the user's cart
    """

    def __init__(self, items: dict[ItemClass, tuple[Decimal, int]]):
        self.inventory: dict[ItemClass, tuple[Decimal, int]] = items
        self.cart: dict[ItemClass, tuple[Decimal, int]] = {}

    def inventory_print(self):
        """Print this Shop's inventory

        Parameters:
            None

        Returns:
            None
        """
        for item, metadata in self.inventory.items():
            print(f"{item}: {metadata}")

    def add_to_cart(self, item: ItemClass, price: Decimal, amount: int):
        """Add a specific item to cart

        Parameters:
            item: ItemClass = The item to add to cart
            price: Decimal = The price of the item as taken from the store
            amount: int = The number of the item to add to cart

        Returns:
            None
        """
        self.cart[item] = (price, amount)

    def remove_from_cart(self, item_name: str):
        """Remove a specific item from cart by name

        Parameters:
            item_name: str = Name of the item to remove from cart

        Returns:
            None
        """
        match: list[ItemClass] = [item for item in self.cart if item.name == item_name]
        if match:
            removed_item = self.cart.pop(match[0])
            print(f"Removed {removed_item[1]}x {match[0]} from cart.")

    def print_inventory(self):
        """Print this stores inventory and stock

        Parameters:
            None

        Returns:
            None
        """
        for item, metadata in self.inventory.items():
            print(f"{item}: {metadata[1]} * ${metadata[0]:.2f}")

    def cart_print(self):
        """Print the items saved in the user's cart

        Parameters:
            None

        Returns:
            None
        """
        total_price = Decimal(0)
        for item, metadata in self.inventory.items():
            total_price += metadata[0]
            print(f"{item}: {metadata[1]} * ${metadata[0]:.2f}")
        print(f"Total price: {total_price:.2f}")

    def buy_cart(self, user: PlayerClass):
        """Buy the player's cart and save it to the player's .inventory

        Parameters:
            user: PlayerClass

        Returns:
            None
        """
        total_price = Decimal(0)
        print("Your cart:")
        for item, metadata in self.cart.items():
            total_price += metadata[0]
            print(f"{item}: {metadata[1]} * ${metadata[0]:.2f}")
        print(f"Your cart costs ${total_price:.2f}.")
        if user.wallet > total_price:
            print(
                f"Buying your cart will leave you with ${(user.wallet - total_price):.2f}"
            )
            if input("Would you like to buy your cart? (y/n)> ").lower()[0] == "y":
                for item, metadata in self.cart.items():
                    user.inventory[item] = metadata[1]
