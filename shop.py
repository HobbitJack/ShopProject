"""Shop class. Main logic for this project."""
import user as ur
import item as it


class ShopItem(it.Item):
    """ShopItem class containing just what is needed to have a working shop.

    Subclasses From:
        item.Item

    Attributes:
        name: str = The name of the item
        price: float = The price of the item
        amount: int = The amount of the item for sale
        durability: int: The percent durability of the item

    Methods:
        None
    """

    def __init__(self, name: str, price: float, amount: int, durability=-1):
        super().__init__(name, durability)
        self.price = price
        self.amount = amount


class Shop:
    """Shop class contairing the primary logic for this project

    Atrributes:
        inventory: list[ShopItem] = The shops inventory of items to sell
        cart: Cart = This shops current cart of items waiting to be sold

    Methods:
        print_store_inventory() -> None: Print all items in the store's
            inventory and clear items with no remaining stock
        add_to_cart(item_name: str, amount: int) -> None: Add the specified
            item to cart at the specified quantity
        purchase_cart(user: user.User) -> None: Purchase the entire cart
            using the specified user's account
    """

    def __init__(
        self,
        item_names: list[str],
        item_prices: list[float],
        item_amounts: list[int],
        item_durabilities: list[int],
    ):
        self.inventory: list[ShopItem] = [
            ShopItem(name, price, amount, durability)
            for name, price, amount, durability in zip(
                item_names, item_prices, item_amounts, item_durabilities
            )
        ]
        self.cart: Cart = Cart()

    def print_store_inventory(self) -> None:
        """Print the store's inventory and remove items with no stock

        Parameters:
            None

        Returns:
            Nothing
        """
        remove_list = []
        for item in self.inventory:
            if item.amount == 0:
                remove_list.append(item)

        for item in remove_list:
            self.inventory.remove(item)

        for item in self.inventory:
            print(f"{item.name}: ${item.price:.2f}, {item.amount}x")

    def add_to_cart(self, item_name: str, amount: int) -> None:
        """Add the specified item to cart at the specified quantity

        Parameters:
            item_name: str = Name of the shop item to add to cart
            amount: int = Quantity of items of the specified type to add to cart

        Returns:
            Nothing
        """
        for item in self.inventory:
            if item.name.lower() == item_name:
                target_item = ShopItem(item.name, item.price, amount, item.durability)

        self.cart.items.append(target_item)

        if amount > target_item.amount:
            print("Quantity to add to cart must not exceed quantity availible!")
            return

        print("Your cart:")
        self.cart.print_cart()

    def purchase_cart(self, user: ur.User) -> None:
        """Purchase the entire cart for the specified user

        Parameters:
            user: user.User = User to purchase cart for

        Returns:
            Nothing
        """
        total_price: float = 0
        for item in self.cart.items:
            total_price += item.price * item.amount
            print(f"{item.name}: ${item.price:.2f}, {item.amount}x")
        if total_price > user.wallet:
            print("You cannot afford to buy your cart")
            return

        print(
            f"Cart sums to ${total_price:.2f}. "
            f"You will be left with ${(user.wallet - total_price):.2f}"
        )
        if input("Would you like to buy your cart? (y/n)\n\n> ")[0].lower() == "y":
            user.wallet -= total_price
            for item in self.cart.items:
                user.inventory[it.Item(item.name, item.durability)] = item.amount
                for shop_item in self.inventory:
                    if shop_item.name == item.name:
                        shop_item.amount -= item.amount
            self.cart.items.clear()


class Cart:
    """Cart class for storing items the user is waiting to buy.

    Attributes:
        items: list[ShopItem] = List of the items in the cart

    Methods:
        print_cart() -> None: Print all items in the cart and clear items with no quantity
    """

    def __init__(self):
        self.items: list[ShopItem] = []

    def remove_item(self, item_name):
        """Remove an item from cart

        Parameters:
            item_name: Name of the item to remove from cart

        Returns:
            None
        """
        for item in self.items:
            if item.name.lower() == item_name:
                target_item = item
                break
        else:
            print("Item to remove not found in cart")
            return
        self.items.remove(target_item)
        self.print_cart()

    def print_cart(self) -> None:
        """Print all items in the cart and clear items with no quantity

        Parameters:
            None

        Returns:
            Nothing
        """
        if len(self.items) > 0:
            remove_list = []
            for item in self.items:
                if item.amount == 0:
                    remove_list.append(item)
            for item in remove_list:
                self.items.remove(item)

        if len(self.items) > 0:
            total_price: float = 0
            for item in self.items:
                total_price += item.price * item.amount
                print(f"{item.name}: ${item.price:.2f}, {item.amount}x")
            print(f"Cart sums to ${total_price:.2f}")
        else:
            print("Cart is empty.")
