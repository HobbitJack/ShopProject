"""This module implements our Shop and its logic."""
from decimal import Decimal
from typing import TypeVar, Generic, Protocol


class ItemHasAttributes(Protocol):
    name: str
    durability: float


ItemClass = TypeVar("ItemClass", bound=ItemHasAttributes)


class PlayerHasAttributes(Generic[ItemClass], Protocol):
    wallet: Decimal
    inventory: dict[ItemClass, int]


PlayerClass = TypeVar("PlayerClass", bound=PlayerHasAttributes)


class Shop(Generic[ItemClass, PlayerClass]):
    def __init__(self, items: dict[ItemClass, tuple[Decimal, int]]):
        self.inventory: dict[ItemClass, tuple[Decimal, int]] = items
        self.cart: dict[ItemClass, tuple[Decimal, int]] = {}

    def inventory_print(self):
        for item, metadata in self.inventory.items():
            print(f"{item}: {metadata}")

    def add_to_cart(self, item: ItemClass, price: Decimal, amount: int):
        self.cart[item] = (price, amount)

    def remove_from_cart(self, item_name: str):
        match: list[ItemClass] = [item for item in self.cart if item.name == item_name]
        if match:
            self.cart.pop(match[0])

    def print_inventory(self):
        for item, metadata in self.inventory.items():
            print(f"{item}: {metadata[1]} * ${metadata[0]:.2f}")

    def cart_print(self):
        total_price = Decimal(0)
        for item, metadata in self.inventory.items():
            total_price += metadata[0]
            print(f"{item}: {metadata[1]} * ${metadata[0]:.2f}")
        print(f"Total price: {total_price:.2f}")

    def buy_cart(self, user: PlayerClass):
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
