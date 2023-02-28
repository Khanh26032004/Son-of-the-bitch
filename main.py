class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Item {self.name} with a price: {self.price: .2f} and quantity: {self.quantity}'


class Cart:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        items_str = ""
        for item in self.items:
            items_str += f'\n{str(item)}'

        return f"Cart with the following items:{items_str}"

    def total_cost(self):
        total = 0
        for i in self.items:
            total += i.price * i.quantity
        total_cost = total
        return round(total_cost, 2)

    def add_item(self, item):
        return self.items.append(item)


class DiscountedCart(Cart):
    def __init__(self, discount_percentage, items):
        super().__init__(items)
        self.discount_percentage = discount_percentage

    def __str__(self):
        items_str = ""
        for item in self.items:
            items_str += f'\n{str(item)}'
        return (f"DiscountedCart with a {self.discount_percentage:.2f}% discount and the following items:"
                f"{items_str}")

    def total_cost(self):
        total = 0
        for i in self.items:
            total += i.price * i.quantity
        total_cost = total * (1 - (self.discount_percentage / 100))
        return round(total_cost, 2)


if __name__ == '__main__':
    discounted_cart = DiscountedCart(10.5, [])
    item1 = Item(name="Apple", price=0.99, quantity=2)
    item2 = Item(name="Banana", price=0.59, quantity=3)
    discounted_cart.add_item(item1)
    discounted_cart.add_item(item2)
    print(discounted_cart.total_cost())  # 3.36

    print(discounted_cart)  # DiscountedCart with a 10.50% discount and the following items:
# Item Apple with a price: 0.99 and quantity: 2
# Item Banana with a price: 0.59 and quantity: 3