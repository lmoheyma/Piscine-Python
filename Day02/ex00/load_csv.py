import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    try:
        data = pd.read_csv(path)
    except IOError:
        print(f"Can't open file {path}")
        return None
    print(f"Loading dataset of dimensions {data.shape}")
    return data
