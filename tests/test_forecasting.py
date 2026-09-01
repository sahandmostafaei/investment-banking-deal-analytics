import pandas as pd

from src.forecasting import forecast_revenue


def test_revenue_forecast():

    df = pd.DataFrame({
        "year": [2024, 2025],
        "revenue": [1000, 1100],
    })

    result = forecast_revenue(
        df,
        years=3,
        growth_rate=0.10,
    )

    assert len(result) == 3

    assert result.iloc[0]["year"] == 2026

    assert result.iloc[0]["revenue"] > 1100
