# Maimuna Murad
# 2065973
# Lab 10.19 Online shopping cart (Part 2)


class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                self.cart_items[i].item_quantity = item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("OUTPUT SHOPPING CART")
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Number of Items: 0\n")
            print("SHOPPING CART IS EMPTY\n")
            print("Total: $0\n")
            return

        else:
            print("OUTPUT SHOPPING CART")
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Number of Items:", self.get_num_items_in_cart())
            print()
            for item in self.cart_items:
                total_item_cost = item.item_quantity * item.item_price
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.0f} = ${total_item_cost:.0f}")

            total_cost = self.get_cost_of_cart()
            print("\nTotal: ${:.0f}\n".format(total_cost))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()


if __name__ == "__main__":
    print("Enter customer's name:")
    input_customer_name = input()
    print("Enter today's date:")
    input_current_date = input()
    print("\nCustomer name:", input_customer_name)
    print("Today's date:", input_current_date)
    print()

    shopping_cart = ShoppingCart(input_customer_name, input_current_date)

    print_menu()
    choice = input("Choose an option:\n").lower()

    while choice != 'q':
        if choice == 'a':
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            shopping_cart.add_item(ItemToPurchase(name, description, price, quantity))
            print()
            print_menu()
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(name)
            print()
            print_menu()
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            shopping_cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))
            print()
            print_menu()
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            shopping_cart.print_descriptions()
            print()
            print_menu()
        elif choice == 'o':
            shopping_cart.print_total()
            print_menu()

        choice = input("Choose an option:\n").lower()

