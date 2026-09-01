from src.sensitivity import dcf_sensitivity


def test_dcf_sensitivity():

    cash_flows = [
        100,
        110,
        120,
        130,
        140,
    ]

    result = dcf_sensitivity(
        cash_flows,
        wacc_values=[
            0.08,
            0.09,
            0.10,
        ],
        growth_values=[
            0.02,
            0.03,
            0.04,
        ],
    )

    assert result.shape == (3, 3)

    assert result.loc[0.08, 0.02] > 0

    assert result.loc[0.09, 0.03] > 0

    assert result.loc[0.10, 0.04] > 0
