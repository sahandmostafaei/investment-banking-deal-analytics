import pandas as pd


def load_precedents(path):
    return pd.read_csv(path)


def calculate_transaction_multiples(df):
    df = df.copy()

    df["ev_revenue"] = (
        df["deal_value"] / df["target_revenue"]
    )

    df["ev_ebitda"] = (
        df["deal_value"] / df["target_ebitda"]
    )

    return df


def calculate_median_multiples(df):
    return {
        "ev_revenue": df["ev_revenue"].median(),
        "ev_ebitda": df["ev_ebitda"].median(),
    }
