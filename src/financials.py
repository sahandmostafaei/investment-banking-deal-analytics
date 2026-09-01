import pandas as pd


def load_financials(path):
    return pd.read_csv(path)


def calculate_financial_metrics(df):
    df = df.copy()

    df["gross_profit"] = df["revenue"] - df["cogs"]

    df["ebitda"] = (
        df["gross_profit"] - df["operating_expenses"]
    )

    df["ebit"] = df["ebitda"] - df["da"]

    df["nopat"] = df["ebit"] * (1 - df["tax_rate"])

    df["unlevered_fcf"] = (
        df["nopat"]
        + df["da"]
        - df["capex"]
        - df["change_nwc"]
    )

    return df


if __name__ == "__main__":

    financials = load_financials(
        "data/company_financials.csv"
    )

    financials = calculate_financial_metrics(
        financials
    )

    print(financials)
