from decimal import Decimal
from collections import namedtuple
from inventory_item import Item
import store


def main():
    items: list[Item] = []

    # These items can be anything:tm: and this data could be pre-processed into a tuple(Item, Decimal, int) and added to item_data
    item_names = ["Sword", "Bow", "Arrow"]
    item_durabilities = [0, 0, 0]
    item_prices = [Decimal("20.00"), Decimal("10.00"), Decimal("1.00")]
    item_amounts = [1, 2, 25]
    for name, durability in zip(item_names, item_durabilities):
        items.append(Item(name, durability))
    ShopItem = namedtuple("ShopItem", ["price", "amount"])
    item_data: list[tuple[Item, Decimal, int]] = [
        (item, price, amount)
        for item, price, amount in zip(items, item_prices, item_amounts)
    ]
    # End shop inventory pre-processing

    current_store = store.Shop(
        {
            item_data[i][0]: ShopItem(item_data[i][1], item_data[i][2])
            for i in range(len(item_data))
        }
    )


def cli(target_store):
    print("Type 'help' for a list of commands.")
    while True:
        command = input("> ").split()
        match command:
            case [str, int]:
                pass
            case ["help"]:
                print("help!")


if __name__ == "__main__":
    main()
