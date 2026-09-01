import pandas as pd

from src.financials import (
    calculate_financial_metrics,
)


def test_financial_metrics():

    df = pd.DataFrame({
        "year": [2025],
        "revenue": [1000],
        "cogs": [600],
        "operating_expenses": [150],
        "da": [50],
        "capex": [40],
        "change_nwc": [20],
        "tax_rate": [0.25],
    })

    result = calculate_financial_metrics(
        df
    )

    assert result.loc[0, "gross_profit"] == 400

    assert result.loc[0, "ebitda"] == 250

    assert result.loc[0, "ebit"] == 200

    assert result.loc[0, "nopat"] == 150

    assert result.loc[0, "unlevered_fcf"] == 140
