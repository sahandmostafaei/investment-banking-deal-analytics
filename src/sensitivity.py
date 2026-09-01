import pandas as pd

from dcf import calculate_dcf


def dcf_sensitivity(
    cash_flows,
    wacc_values,
    growth_values,
):
    results = []

    for wacc in wacc_values:

        row = []

        for growth in growth_values:

            if growth >= wacc:
                row.append(None)
                continue

            valuation = calculate_dcf(
                cash_flows,
                wacc=wacc,
                terminal_growth=growth,
            )

            row.append(
                valuation["enterprise_value"]
            )

        results.append(row)

    return pd.DataFrame(
        results,
        index=wacc_values,
        columns=growth_values,
    )
