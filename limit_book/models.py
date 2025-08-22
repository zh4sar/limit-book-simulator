class OrderLevel:
    def __init__(self, price, amount):
        self.price = float(price)
        self.amount = float(amount)

    def __repr__(self):
        return f"OrderLevel(price={self.price}, amount={self.amount})"
