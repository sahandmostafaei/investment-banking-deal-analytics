from src.merger_model import calculate_merger


def test_merger_model():

    result = calculate_merger(
        buyer_net_income=500,
        target_net_income=100,
        purchase_price=2000,
        cash_financing=500,
        debt_financing=1000,
        stock_financing=500,
        interest_rate=0.05,
        tax_rate=0.25,
        synergies=50,
        buyer_shares=100,
        new_shares=10,
    )

    assert result["pro_forma_net_income"] > 0

    assert result["pro_forma_eps"] > 0

    assert "accretion_dilution" in result
