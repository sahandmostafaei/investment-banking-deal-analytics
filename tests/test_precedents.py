import pandas as pd

from src.precedents import (
    calculate_transaction_multiples,
    calculate_median_multiples,
)


def test_precedent_transaction_multiples():

    df = pd.DataFrame({
        "transaction": [
            "Deal A",
            "Deal B",
        ],
        "deal_value": [
            2000,
            3000,
        ],
        "target_revenue": [
            1000,
            1200,
        ],
        "target_ebitda": [
            200,
            300,
        ],
    })

    result = calculate_transaction_multiples(
        df
    )

    assert "ev_revenue" in result.columns

    assert "ev_ebitda" in result.columns

    medians = calculate_median_multiples(
        result
    )

    assert medians["ev_revenue"] > 0

    assert medians["ev_ebitda"] > 0
