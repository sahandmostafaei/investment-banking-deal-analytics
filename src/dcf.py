import numpy as np


def calculate_dcf(
    cash_flows,
    wacc=0.09,
    terminal_growth=0.03,
):
    cash_flows = np.array(cash_flows, dtype=float)

    periods = np.arange(
        1,
        len(cash_flows) + 1,
    )

    present_values = (
        cash_flows
        / (1 + wacc) ** periods
    )

    terminal_value = (
        cash_flows[-1]
        * (1 + terminal_growth)
        / (wacc - terminal_growth)
    )

    terminal_pv = (
        terminal_value
        / (1 + wacc) ** len(cash_flows)
    )

    enterprise_value = (
        present_values.sum()
        + terminal_pv
    )

    return {
        "present_values": present_values,
        "terminal_value": terminal_value,
        "terminal_pv": terminal_pv,
        "enterprise_value": enterprise_value,
    }
