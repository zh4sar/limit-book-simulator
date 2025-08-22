import pandas as pd

class CSVLoader:
    REQUIRED_COLUMNS = ['s_price', 's_amount', 'b_price', 'b_amount']

    def load(self, filepath):
        df = pd.read_csv(filepath)
        missing = [x for x in self.REQUIRED_COLUMNS if x not in df.columns]
        if missing:
            raise ValueError(f"CSV is missing required columns: {missing}")
        return df[self.REQUIRED_COLUMNS].copy()
