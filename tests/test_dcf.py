from src.dcf import calculate_dcf


def test_dcf_returns_enterprise_value():

    cash_flows = [
        100,
        110,
        120,
        130,
        140,
    ]

    result = calculate_dcf(
        cash_flows,
        wacc=0.09,
        terminal_growth=0.03,
    )

    assert "enterprise_value" in result

    assert result["enterprise_value"] > 0
