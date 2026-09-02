import pandas as pd

from src.export import export_valuation_workbook


def test_export_valuation_workbook(tmp_path):

    financials = pd.DataFrame({
        "year": [2025],
        "revenue": [1000],
    })

    forecast = pd.DataFrame({
        "year": [2026],
        "revenue": [1080],
    })

    comparables = pd.DataFrame({
        "company": ["Company A"],
        "ev_ebitda": [10.0],
    })

    precedents = pd.DataFrame({
        "transaction": ["Deal A"],
        "ev_ebitda": [12.0],
    })

    sensitivity = pd.DataFrame(
        [[5000, 5200]],
        index=[0.09],
        columns=[0.02, 0.03],
    )

    output_path = (
        tmp_path / "valuation.xlsx"
    )

    export_valuation_workbook(
        financials,
        forecast,
        comparables,
        precedents,
        sensitivity,
        output_path,
    )

    assert output_path.exists()
