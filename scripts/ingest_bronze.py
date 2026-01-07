import pandas as pd

def ingest_to_bronze():
    df = pd.read_csv("data/raw_sales.csv")
    df.to_parquet(
        "s3://bucket-bronze/sales/",
        engine="pyarrow",
        index=False
    )
