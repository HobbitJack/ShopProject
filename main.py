"""Demo CLI for the store. Not necessary."""
from decimal import Decimal

from inventory_item import Item
from player import Player
import store


def main():
    """Main Function for the demo CLI

    Parameters:
        None

    Returns:
        None
    """
    item_data: dict[Item, tuple[Decimal, int]]
    user = Player(Decimal(100), {})

    # These items can be anything:tm: and this data could be
    # pre-processed into a tuple(Item, Decimal, int) and added to item_data

    item_names = ["Sword", "Bow", "Arrow"]
    item_durabilities = [100, 100, -1]
    item_prices = [Decimal("20.00"), Decimal("10.00"), Decimal("1.00")]
    item_amounts = [1, 2, 25]

    item_data = {
        Item(name, durability): (price, amount)
        for name, durability, price, amount in zip(
            item_names, item_durabilities, item_prices, item_amounts
        )
    }
    # End shop inventory pre-processing

    cli(store.Shop(item_data), user)


def add_to_cart(shop: store.Shop, command: list[str]):
    """Add a specified item to cart at a specific amount

    Parameters:
        shop: store.Shop = Shop to take items from and to store cart to
        command: list[str] = Item name and amount to add to cart

    Returns:
        None
    """
    if len(command) == 2:
        try:
            amount = int(command[1])
            assert amount > 0
        except (ValueError, AssertionError):
            print("Quantity to add to cart must be a positive integer.")
            return
        for item, metadata in shop.inventory.items():
            if item.name == command[0]:
                if amount < metadata[1]:
                    print("Quantity to add to cart must not exceed quantity availible.")
                    return
                shop.add_to_cart(item, metadata[0], amount)


def print_help():
    """Print help information about the CLI

    Parameters:
        None

    Returns:
        None
    """
    print(
        "Type an item name, with capitalization and punctuation,"
        "followed by a number to add that many of that item to cart"
    )
    print("buy: Purchase all items in your cart")
    print("help: Describe how to use this program")
    print("items: Print the store's stock of items to buy")
    print("quit: Exit this program")
    print(
        "remove [item name]: Remove all instances of the item with that name from your cart"
    )


def cli(target_store: store.Shop, target_user: Player):
    """Demo command line interface

    Parameters:
        target_store: store.Shop = Store to buy items from
        target_user: Player = Player to buy for

    Returns:
        None
    """
    print("Type 'help' for a list of commands.")
    while True:
        command = input("> ").split()
        if command[0] in [item.name for item in target_store.inventory.keys()]:
            add_to_cart(target_store, command)
            target_store.cart_print()
            break
        match command:
            case ["buy"]:
                target_store.buy_cart(target_user)
            case ["help"]:
                print_help()
            case ["items"]:
                target_store.print_inventory()
            case ["inventory"]:
                print(target_user.inventory)
            case ["quit"]:
                break
            case ["remove", item_name]:
                target_store.remove_from_cart(item_name)
            case _:
                print("Unrecognized command.")


if __name__ == "__main__":
    main()
