class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["price"] * transaction["quantity"]

        for _ in range(transaction["quantity"]):
            if len(self.items) > 0:
                self.items.pop()

        if len(self.items) == 0:
            self.total = 0.0
