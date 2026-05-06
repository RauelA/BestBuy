
class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str) or name == "":
            raise ValueError("Invalid product name")

        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Invalid price")

        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True if quantity > 0 else False


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        try:
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer")

            if quantity > self.quantity:
                print("Error: Not enough stock")
                return False

            if not self.active:
                print("Error: Product is inactive")
                return False

            self.quantity -= quantity

            if self.quantity == 0:
                self.deactivate()

            return float(self.price * quantity)

        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
            return False