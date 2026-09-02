from src.valuation_summary import build_valuation_summary


def test_valuation_summary():

    result = build_valuation_summary(
        dcf_value=5000,
        comparable_value=5200,
        precedent_value=5400,
    )

    assert result["dcf_enterprise_value"] == 5000

    assert result["comparable_enterprise_value"] == 5200

    assert result["precedent_enterprise_value"] == 5400

    assert result["average_enterprise_value"] == 5200
