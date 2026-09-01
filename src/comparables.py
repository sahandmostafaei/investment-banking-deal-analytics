import pandas as pd


def load_comparables(path):
    return pd.read_csv(path)


def calculate_trading_multiples(df):
    df = df.copy()

    df["ev_revenue"] = (
        df["enterprise_value"] / df["revenue"]
    )

    df["ev_ebitda"] = (
        df["enterprise_value"] / df["ebitda"]
    )

    df["pe_ratio"] = (
        df["market_cap"]
        / (
            df["ebitda"]
            - df["net_debt"] * 0.05
        )
    )

    return df


def calculate_median_multiples(df):
    return {
        "ev_revenue": df["ev_revenue"].median(),
        "ev_ebitda": df["ev_ebitda"].median(),
        "pe_ratio": df["pe_ratio"].median(),
    }


def value_target(
    revenue,
    ebitda,
    net_income,
    multiples,
):
    ev_from_revenue = (
        revenue * multiples["ev_revenue"]
    )

    ev_from_ebitda = (
        ebitda * multiples["ev_ebitda"]
    )

    equity_from_pe = (
        net_income * multiples["pe_ratio"]
    )

    return {
        "ev_from_revenue": ev_from_revenue,
        "ev_from_ebitda": ev_from_ebitda,
        "equity_from_pe": equity_from_pe,
    }
