from .models import OrderLevel

class OrderBook:
    def __init__(self, sell_levels, buy_levels):
        self.sell = sell_levels  # asks
        self.buy = buy_levels    # bids

    @classmethod
    def from_dataframe(cls, df):
        sell_levels = [OrderLevel(p, a) for p, a in zip(df['s_price'], df['s_amount'])]
        buy_levels  = [OrderLevel(p, a) for p, a in zip(df['b_price'], df['b_amount'])]
        return cls(sell_levels, buy_levels)

    def best_ask(self):
        return self.sell[0].price if self.sell else None

    def best_bid(self):
        return self.buy[0].price if self.buy else None

    def spread(self):
        if self.best_ask() is None or self.best_bid() is None:
            return None
        return self.best_ask() - self.best_bid()

    def levels(self, side):
        if side == 'sell':
            return self.sell
        if side == 'buy':
            return self.buy
        raise ValueError("side must be 'sell' or 'buy'")

    def __len__(self):
        return len(self.sell) + len(self.buy)
