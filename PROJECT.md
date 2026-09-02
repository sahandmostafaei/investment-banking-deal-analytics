# Investment Banking Deal Analytics & Valuation Platform

## Overview

A Python-based investment banking analytics platform covering financial statement analysis, forecasting, valuation, comparable companies, precedent transactions, DCF sensitivity analysis, and M&A accretion/dilution.

## Objectives

- Analyze historical financial statements
- Calculate key financial metrics
- Forecast revenue
- Estimate unlevered free cash flow
- Perform DCF valuation
- Analyze trading comparables
- Analyze precedent transactions
- Compare valuation methodologies
- Perform DCF sensitivity analysis
- Model M&A accretion/dilution
- Generate financial visualizations
- Automate financial analysis with Python

## Technology

- Python
- pandas
- NumPy
- SciPy
- Matplotlib
- OpenPyXL
- pytest

## Project Architecture

Company Financial Data
        |
        v
Financial Statement Analysis
        |
        v
Revenue Forecast
        |
        v
DCF Valuation
        |
        +-----------------------+
        |                       |
        v                       v
Comparable Companies     Precedent Transactions
        |                       |
        +-----------+-----------+
                    |
                    v
             Valuation Summary
                    |
                    v
          M&A Accretion/Dilution

## Financial Analysis

The financial analysis module calculates:

- Gross profit
- EBITDA
- EBIT
- NOPAT
- Unlevered free cash flow

## Forecasting

Revenue is projected using a configurable annual growth assumption.

The current implementation produces a five-year revenue forecast.

## DCF Valuation

The DCF model calculates enterprise value using:

- Forecast free cash flows
- WACC
- Terminal growth rate
- Present value calculations
- Gordon Growth terminal value

## Comparable Companies

The trading comparable analysis calculates:

- EV / Revenue
- EV / EBITDA
- P/E-style analysis

Median peer multiples are calculated and applied to target company financial metrics.

## Precedent Transactions

Historical acquisition transactions are analyzed using:

- EV / Revenue
- EV / EBITDA

Median transaction multiples are applied to target financial metrics to estimate an implied transaction value.

## Valuation Summary

The valuation summary combines three valuation perspectives:

1. DCF valuation
2. Comparable company valuation
3. Precedent transaction valuation

An average enterprise value is calculated from the three approaches.

## DCF Sensitivity Analysis

Enterprise value is evaluated across multiple combinations of:

- WACC
- Terminal growth rate

The resulting sensitivity matrix is also visualized.

## M&A Accretion / Dilution

The merger model evaluates the effect of an acquisition on buyer EPS.

Inputs include:

- Buyer net income
- Target net income
- Purchase price
- Cash financing
- Debt financing
- Stock financing
- Interest rate
- Tax rate
- Synergies
- Buyer shares
- New shares issued

Outputs include:

- Interest expense
- After-tax interest expense
- Pro forma net income
- Pro forma shares
- Buyer EPS
- Pro forma EPS
- Accretion / dilution

## Visualization

The project generates:

- Revenue forecast chart
- DCF sensitivity visualization

Charts are stored in:

figures/

## Testing

Automated tests cover:

- Financial calculations
- DCF valuation
- Revenue forecasting
- Comparable companies
- Precedent transactions
- M&A modelling
- DCF sensitivity
- Valuation summary
- Utility functions

Testing is implemented using pytest.

## Project Structure

investment-banking-deal-analytics/
|
├── .github/
│   └── workflows/
│       └── tests.yml
|
├── data/
│   ├── company_financials.csv
│   ├── comparable_companies.csv
│   └── precedent_transactions.csv
|
├── figures/
|
├── src/
│   ├── __init__.py
│   ├── financials.py
│   ├── forecasting.py
│   ├── dcf.py
│   ├── comparables.py
│   ├── precedents.py
│   ├── merger_model.py
│   ├── sensitivity.py
│   ├── valuation_summary.py
│   ├── visualization.py
│   └── utils.py
|
├── tests/
│   ├── test_dcf.py
│   ├── test_financials.py
│   ├── test_forecasting.py
│   ├── test_comparables.py
│   ├── test_merger_model.py
│   ├── test_sensitivity.py
│   ├── test_precedents.py
│   ├── test_valuation_summary.py
│   └── test_utils.py
|
├── main.py
├── PROJECT.md
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

## Skills Demonstrated

- Python programming
- Financial modelling
- Corporate finance
- Company valuation
- DCF analysis
- Comparable company analysis
- M&A modelling
- Sensitivity analysis
- Data analysis
- Financial visualization
- Modular software design
- Automated testing

## Disclaimer

This project is intended for educational, research, and portfolio purposes only.

It does not constitute investment advice, financial advice, or a recommendation to buy or sell any security.
