# Investment Banking Deal Analytics & Valuation Platform

A Python-based investment banking analytics platform for financial analysis, valuation, M&A modelling, financial visualization, and Excel-based reporting.

## Overview

This project demonstrates practical applications of Python in investment banking and corporate finance workflows.

Key areas covered:

- Financial statement analysis
- Revenue forecasting
- DCF valuation
- Comparable company analysis
- Precedent transaction analysis
- Valuation methodology comparison
- DCF sensitivity analysis
- M&A accretion/dilution analysis
- Financial visualization
- Excel valuation workbook export
- Automated testing

## Technology Stack

- Python
- pandas
- NumPy
- SciPy
- Matplotlib
- OpenPyXL
- pytest

## Project Workflow

Financial Data
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
Comparable Companies   Precedent Transactions
      |                       |
      +-----------+-----------+
                  |
                  v
           Valuation Summary
                  |
                  v
         M&A Accretion/Dilution
                  |
                  v
          Excel Valuation Report

## Financial Analysis

The financial statement module calculates:

- Revenue
- Gross Profit
- EBITDA
- EBIT
- NOPAT
- Capital Expenditure
- Change in Net Working Capital
- Unlevered Free Cash Flow

## Revenue Forecasting

The forecasting module projects future revenue using an assumed annual growth rate.

The model generates a five-year revenue forecast based on the latest available historical revenue.

## DCF Valuation

The DCF module estimates enterprise value using projected free cash flows, WACC, and terminal growth.

Outputs include:

- Present value of forecast cash flows
- Terminal value
- Present value of terminal value
- Enterprise value

## Comparable Companies Analysis

The comparable companies module analyzes peer companies using valuation multiples.

Key multiples include:

- EV / Revenue
- EV / EBITDA
- P/E-style analysis

Median multiples are calculated and applied to target company financial metrics.

## Precedent Transactions

The precedent transactions module analyzes historical M&A transactions using:

- EV / Revenue
- EV / EBITDA

Median transaction multiples are calculated to provide an acquisition-market valuation reference.

## Valuation Summary

The valuation summary combines:

- DCF enterprise value
- Comparable company enterprise value
- Precedent transaction enterprise value

The model also calculates an average enterprise value across the three approaches.

## DCF Sensitivity Analysis

The sensitivity module evaluates how changes in valuation assumptions affect enterprise value.

The model varies:

- WACC
- Terminal growth rate

A sensitivity matrix is generated and visualized using Matplotlib.

## M&A Accretion / Dilution

The merger model evaluates the potential EPS impact of an acquisition.

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
- Accretion / dilution percentage

## Excel Export

The project includes an Excel export module for creating a structured valuation workbook.

The workbook can contain separate sheets for:

- Financials
- Revenue Forecast
- Comparable Companies
- Precedent Transactions
- DCF Sensitivity

The Excel export is implemented using OpenPyXL through pandas.

## Visualizations

The project generates financial analysis charts in the `figures/` directory.

Revenue forecast:

`figures/revenue_forecast.png`

DCF sensitivity:

`figures/dcf_sensitivity.png`

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
│   ├── export.py
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
│   ├── test_utils.py
│   └── test_export.py
|
├── main.py
├── PROJECT.md
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

## Modules

| Module | Purpose |
|---|---|
| `financials.py` | Financial statement and FCF calculations |
| `forecasting.py` | Revenue forecasting |
| `dcf.py` | DCF valuation |
| `comparables.py` | Trading comparable analysis |
| `precedents.py` | Precedent transaction analysis |
| `merger_model.py` | M&A accretion/dilution |
| `sensitivity.py` | DCF sensitivity analysis |
| `valuation_summary.py` | Combines valuation approaches |
| `visualization.py` | Financial charts |
| `export.py` | Excel valuation workbook export |
| `utils.py` | Output formatting |
| `main.py` | End-to-end analysis pipeline |

## Testing

The project includes automated tests using pytest.

Tests cover:

- DCF valuation
- Financial metric calculations
- Revenue forecasting
- Comparable company calculations
- Precedent transaction calculations
- M&A modelling
- DCF sensitivity analysis
- Valuation summary
- Utility functions
- Excel export

GitHub Actions is configured to run the test suite automatically.

## Key Skills Demonstrated

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
- Excel automation
- Modular software design
- Automated testing

## Purpose

This project demonstrates practical programming applications in investment banking and corporate finance.

It combines financial modelling, valuation analysis, M&A modelling, data analysis, visualization, Excel reporting, and modular Python software development.

## Disclaimer

This project is intended for educational, research, and portfolio purposes only.

It does not constitute investment advice, financial advice, or a recommendation to buy or sell any security.
