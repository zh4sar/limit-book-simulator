
from limit_book import CSVLoader, OrderBook, Simulator, BookPlotter

CSV_PATH = "data/BTCUSD_2019_09_01.csv"

def main():
    loader = CSVLoader()
    df = loader.load(CSV_PATH)

    book = OrderBook.from_dataframe(df)

    print("Best Bid:", book.best_bid())
    print("Best Ask:", book.best_ask())
    print("Spread:", book.spread())

    plotter = BookPlotter()
    plotter.plot_prices(book)

    sim = Simulator(book)

    print("\nSimulate MARKET BUY of 13 units:")
    print(sim.market_buy(13))

    print("\nSimulate MARKET SELL of 300 units:")
    print(sim.market_sell(300))

if __name__ == "__main__":
    main()
