import pandas as pd

def transform_to_silver():
    df = pd.read_parquet("s3://bucket-bronze/sales/")
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["amount"] = df["amount"].astype(float)
    df.dropna(inplace=True)

    df.to_parquet(
        "s3://bucket-silver/sales/",
        engine="pyarrow",
        index=False
    )
