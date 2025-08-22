
import matplotlib.pyplot as plt

class BookPlotter:
    def plot_prices(self, order_book):
        sell_prices = [lvl.price for lvl in order_book.sell]
        buy_prices = [lvl.price for lvl in order_book.buy]

        plt.figure()
        plt.plot(sell_prices, label='Sell (asks)')
        plt.plot(buy_prices, label='Buy (bids)')
        plt.title('Limit Order Book Prices')
        plt.xlabel('Level Index')
        plt.ylabel('Price (USD)')
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()
