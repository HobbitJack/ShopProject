import item as it
import shop as sp
import user as ur


def setup() -> None:
    shop = sp.Shop
    user = ur.User

    item_names = []
    item_prices = []
    item_quantities = []

    items = [it.Item(item_names[i], item_prices[i]) for i in range(len(item_names))]
    inventory = {items[i].name: item_quantities[i] for i in range(len(item_quantities))}

    shop.inventory = inventory


def main() -> None:
    setup()


if __name__ == "__main__":
    main()
