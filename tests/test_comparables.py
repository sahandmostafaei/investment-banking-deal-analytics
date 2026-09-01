import pandas as pd

from src.comparables import (
    calculate_trading_multiples,
    calculate_median_multiples,
)


def test_comparable_multiples():

    df = pd.DataFrame({
        "company": ["A", "B"],
        "revenue": [1000, 1200],
        "ebitda": [200, 240],
        "enterprise_value": [2000, 2400],
        "net_debt": [200, 300],
        "market_cap": [1800, 2100],
    })

    result = calculate_trading_multiples(df)

    assert "ev_revenue" in result.columns
    assert "ev_ebitda" in result.columns
    assert "pe_ratio" in result.columns

    medians = calculate_median_multiples(result)

    assert medians["ev_revenue"] > 0
    assert medians["ev_ebitda"] > 0
