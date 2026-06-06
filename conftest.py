import pandas as pd

def load_metadata():

    df = pd.read_csv(
        "metadata/tables.csv"
    )

    return df.to_dict("records")