import pandas as pd

from src.financials import (
    load_financials,
    calculate_financial_metrics,
)

from src.forecasting import forecast_revenue

from src.dcf import calculate_dcf

from src.comparables import (
    load_comparables,
    calculate_trading_multiples,
    calculate_median_multiples,
    value_target,
)

from src.precedents import (
    load_precedents,
    calculate_transaction_multiples,
    calculate_median_multiples as precedent_median,
)

from src.sensitivity import dcf_sensitivity

from src.merger_model import calculate_merger

from src.utils import (
    format_currency,
    format_percentage,
)

from src.visualization import (
    plot_revenue_forecast,
    plot_dcf_sensitivity,
)


def main():

    print("=" * 70)
    print("INVESTMENT BANKING DEAL ANALYTICS")
    print("=" * 70)

    # --------------------------------------------------
    # Financial Analysis
    # --------------------------------------------------

    financials = load_financials(
        "data/company_financials.csv"
    )

    financials = calculate_financial_metrics(
        financials
    )

    latest = financials.iloc[-1]

    print("\nLATEST FINANCIALS")
    print("-" * 70)

    print(
        "Revenue:",
        format_currency(latest["revenue"])
    )

    print(
        "EBITDA:",
        format_currency(latest["ebitda"])
    )

    print(
        "EBIT:",
        format_currency(latest["ebit"])
    )

    print(
        "Unlevered FCF:",
        format_currency(
            latest["unlevered_fcf"]
        )
    )

    # --------------------------------------------------
    # Revenue Forecast
    # --------------------------------------------------

    forecast = forecast_revenue(
        financials,
        years=5,
        growth_rate=0.08,
    )

    print("\nREVENUE FORECAST")
    print("-" * 70)

    print(
        forecast.to_string(index=False)
    )

    plot_revenue_forecast(
        historical=financials,
        forecast=forecast,
        output_path="figures/revenue_forecast.png",
    )

    # --------------------------------------------------
    # DCF
    # --------------------------------------------------

    forecast_fcf = (
        financials["unlevered_fcf"]
        .iloc[-1]
        * (
            1.08
            ** pd.Series(range(1, 6))
        )
    )

    dcf = calculate_dcf(
        forecast_fcf.values,
        wacc=0.09,
        terminal_growth=0.03,
    )

    print("\nDCF VALUATION")
    print("-" * 70)

    print(
        "Terminal Value:",
        format_currency(
            dcf["terminal_value"]
        ),
    )

    print(
        "Enterprise Value:",
        format_currency(
            dcf["enterprise_value"]
        ),
    )

    # --------------------------------------------------
    # Comparable Companies
    # --------------------------------------------------

    comparables = load_comparables(
        "data/comparable_companies.csv"
    )

    comparables = calculate_trading_multiples(
        comparables
    )

    median_comps = calculate_median_multiples(
        comparables
    )

    target_revenue = float(
        latest["revenue"]
    )

    target_ebitda = float(
        latest["ebitda"]
    )

    target_net_income = float(
        latest["nopat"]
    )

    comparable_value = value_target(
        target_revenue,
        target_ebitda,
        target_net_income,
        median_comps,
    )

    print("\nTRADING COMPARABLES")
    print("-" * 70)

    print(
        "Median EV / Revenue:",
        round(
            median_comps["ev_revenue"],
            2,
        ),
    )

    print(
        "Median EV / EBITDA:",
        round(
            median_comps["ev_ebitda"],
            2,
        ),
    )

    print(
        "Implied EV from Revenue:",
        format_currency(
            comparable_value[
                "ev_from_revenue"
            ]
        ),
    )

    print(
        "Implied EV from EBITDA:",
        format_currency(
            comparable_value[
                "ev_from_ebitda"
            ]
        ),
    )

    # --------------------------------------------------
    # Precedent Transactions
    # --------------------------------------------------

    precedents = load_precedents(
        "data/precedent_transactions.csv"
    )

    precedents = calculate_transaction_multiples(
        precedents
    )

    median_precedents = precedent_median(
        precedents
    )

    print("\nPRECEDENT TRANSACTIONS")
    print("-" * 70)

    print(
        "Median EV / Revenue:",
        round(
            median_precedents[
                "ev_revenue"
            ],
            2,
        ),
    )

    print(
        "Median EV / EBITDA:",
        round(
            median_precedents[
                "ev_ebitda"
            ],
            2,
        ),
    )

    # --------------------------------------------------
    # DCF Sensitivity
    # --------------------------------------------------

    sensitivity = dcf_sensitivity(
        forecast_fcf.values,
        wacc_values=[
            0.07,
            0.08,
            0.09,
            0.10,
            0.11,
        ],
        growth_values=[
            0.02,
            0.025,
            0.03,
            0.035,
            0.04,
        ],
    )

    print("\nDCF SENSITIVITY")
    print("-" * 70)

    print(
        sensitivity.round(2).to_string()
    )

    plot_dcf_sensitivity(
        sensitivity,
        output_path="figures/dcf_sensitivity.png",
    )

    # --------------------------------------------------
    # M&A Accretion / Dilution
    # --------------------------------------------------

    merger = calculate_merger(
        buyer_net_income=500,
        target_net_income=120,
        purchase_price=2500,
        cash_financing=500,
        debt_financing=1000,
        stock_financing=1000,
        interest_rate=0.05,
        tax_rate=0.25,
        synergies=40,
        buyer_shares=100,
        new_shares=20,
    )

    print("\nM&A ACCRETION / DILUTION")
    print("-" * 70)

    print(
        "Pro Forma EPS:",
        format_currency(
            merger["pro_forma_eps"]
        ),
    )

    print(
        "Accretion / Dilution:",
        format_percentage(
            merger["accretion_dilution"]
        ),
    )

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
