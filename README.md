
## Setup

```bash
cd limit_book_project
python -m venv .venv
pip install -r requirements.txt
```

## Run
```bash
# sample data can be changed with YFinance
python main.py data/BTCUSD_2019_09_01.csv
```

Or run the example script
```bash
python scripts/run_example.py
```

## Tests
```bash
pytest -q
```

## Notes
- The simulator **does not mutate** the order book. It only computes what would happen for a given market order size.
