
import products

class Store:
    def __init__(self, products):
        self.products = products


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self):
        return [product for product in self.products if product.is_active()]


    @staticmethod
    def order(shopping_list):
        total_price = 0

        for product, quantity in shopping_list:
            result = product.buy(quantity)
            if result is False:
                continue
            total_price += result

        return float(total_price)
