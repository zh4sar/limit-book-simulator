import pandas as pd
from limit_book import OrderBook, Simulator

def test_spread_basic():
    data = {
        's_price': [105, 106],
        's_amount': [5, 10],
        'b_price': [100, 99],
        'b_amount': [3, 7]
    }
    df = pd.DataFrame(data)
    book = OrderBook.from_dataframe(df)
    assert book.best_ask() == 105
    assert book.best_bid() == 100
    assert book.spread() == 5

def test_simulator_fill():
    data = {
        's_price': [101, 102],
        's_amount': [5, 10],
        'b_price': [100, 99],
        'b_amount': [3, 7]
    }
    df = pd.DataFrame(data)
    book = OrderBook.from_dataframe(df)
    sim = Simulator(book)
    result = sim.market_buy(8)  # should consume 5 at 101 and 3 at 102
    assert result['filled'] == 8
    assert result['levels_used'] == 2
    assert result['last_price'] == 102
