import pandas as pd

def aggregate_gold():
    df = pd.read_parquet("s3://bucket-silver/sales/")
    gold = df.groupby("region")["amount"].sum().reset_index()

    gold.to_parquet(
        "s3://bucket-gold/sales_metrics/",
        engine="pyarrow",
        index=False
    )
