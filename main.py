import products
import store


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = store.Store(product_list)


def start(store_obj):
    """
    This function is used to show and handle the main menu.
    It runs different cases based on the input number.
    """
    while True:
        print("\n=== STORE MENU ===")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == "1":
            print("")
            for p in store_obj.get_all_products():
                p.show()

        elif choice == "2":
            total = store_obj.get_total_quantity()
            print("Total quantity in store:", total)

        elif choice == "3":
            shopping_list = []

            print("\nEnter product number and quantity.")
            print("(When you want to finish order, press Enter.)\n")

            products = store_obj.get_all_products()

            for i, product in enumerate(products):
                print(f"{i + 1}: {product.name} (Price: {product.price}, Stock: {product.quantity})")

            while True:
                try:
                    product_index = input("\nWhich product do you want?: ")

                    if product_index == "":
                        break

                    product_index = int(product_index)

                    if product_index < 1 or product_index > len(products):
                        print("Invalid product number")
                        continue

                    quantity = input("What amount do you want?: ")

                    if quantity == "":
                        break

                    quantity = int(quantity)

                    shopping_list.append((products[product_index - 1], quantity))

                except ValueError:
                    print("Invalid input, try again.")

            total_price = store_obj.order(shopping_list)
            print(f"********\nOrder made! Total payment: ${total_price}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


def main():
    """
    The main function, called once at start.
    """
    store_obj = store.Store(product_list)
    start(store_obj)


if __name__ == "__main__":
    main()