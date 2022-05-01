"""Simple command line interface to hold the shop system together"""
import shop as sp
import user as ur

VERSION = (1, 2)


def print_help() -> None:
    """Prints all available commands

    Parameters:
        None

    Returns:
        Nothing
    """
    print("buy: Allows you to purchase the items in your cart")
    print("cart: Prints the your cart and its total price")
    print("help: Prints the list of availible commands")
    print("inventory: Prints your inventory and how much money you have")
    print("items: Prints all items availible for sale")
    print("quit: Exits the shop")


def cli(user: ur.User, shop: sp.Shop) -> None:
    """Primary CLI function for user interation. Can easily be re-written to suit anyone's needs.

    Parameters:
        user: user.User = Player object to get money from and acess inventory
        shop: shop.Shop = Shop object with given inventory to sell from

    Returns:
        Nothing
    """
    print(f"Shop Project Mark {VERSION[0]} Mod {VERSION[1]}\n")
    print("Type 'help' for a list of commands.")
    while True:
        command = str(input("\n> ")).split(" ")
        if command[0] in [item.name.lower() for item in shop.inventory]:
            if len(command) == 2:
                shop.add_to_cart(command[0], int(command[1]))
            else:
                print("Please include a quantity to add to cart.")

        else:
            match command[0]:
                case "buy":
                    shop.purchase_cart(user)
                    print("Your inventory:")
                    user.print_inventory()

                case "cart":
                    shop.cart.print_cart()

                case "help":
                    print_help()

                case "inventory":
                    user.print_inventory()

                case "items":
                    shop.print_store_inventory()

                case "quit":
                    break

                case "remove":
                    if len(command) != 2:
                        print("Please specify an item to remove from your cart.")
                    else:
                        shop.cart.remove_item(command[1])

                case _:
                    print("Unrecognized command.")
            continue


def main() -> None:
    """Entry point for demo

    Parameters:
        None

    Returns:
        Nothing
    """
    store: sp.Shop = sp.Shop(
        ["Sword", "Bow", "Arrows"], [10, 5, 1], [1, 2, 50], [100, 100, -1]
    )
    player: ur.User = ur.User(100)

    cli(player, store)
    print(f"Thank you for using Shop Project Mark {VERSION[0]} Mod {VERSION[1]}\n")


if __name__ == "__main__":
    main()
