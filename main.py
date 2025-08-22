
import sys
from limit_book import CSVLoader, OrderBook, Simulator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_lob_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]

    loader = CSVLoader()
    df = loader.load(csv_path)
    book = OrderBook.from_dataframe(df)

    print("Best Bid:", book.best_bid())
    print("Best Ask:", book.best_ask())
    print("Spread:", book.spread())

    sim = Simulator(book)
    print("\nExample: MARKET BUY 10 units:")
    print(sim.market_buy(10))

if __name__ == "__main__":
    main()
