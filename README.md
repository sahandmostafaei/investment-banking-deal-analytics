# Investment Banking Deal Analytics & Valuation Platform

A Python-based investment banking analytics platform for financial analysis, valuation, and M&A modelling.

## Overview

This project demonstrates the use of Python in investment banking and corporate finance workflows.

Key areas covered:

- Financial statement analysis
- Revenue forecasting
- DCF valuation
- Comparable company analysis
- Precedent transaction analysis
- DCF sensitivity analysis
- M&A accretion/dilution analysis
- Financial visualization
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

Financial Data → Financial Statement Analysis → Revenue Forecast → DCF Valuation → Comparable Companies → Precedent Transactions → Sensitivity Analysis → M&A Analysis

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

Median multiples are calculated and applied to the target company's financial metrics.

## Precedent Transactions

The precedent transactions module analyzes historical M&A transactions using:

- EV / Revenue
- EV / EBITDA

Median transaction multiples are calculated to provide an acquisition-market valuation reference.

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

## Visualizations

The project generates financial analysis charts in the `figures/` directory.

### Revenue Forecast

`figures/revenue_forecast.png`

### DCF Sensitivity

`figures/dcf_sensitivity.png`

## Project Structure

- `data/` — Financial and transaction datasets
- `src/` — Financial modelling modules
- `figures/` — Generated charts
- `tests/` — Automated tests
- `main.py` — End-to-end analysis pipeline
- `PROJECT.md` — Project documentation
- `requirements.txt` — Python dependencies
- `.gitignore` — Git configuration

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
| `visualization.py` | Financial charts |
| `utils.py` | Output formatting |
| `main.py` | End-to-end analysis pipeline |

## Testing

The project includes automated tests using pytest.

Tests cover:

- DCF valuation
- Financial metric calculations
- Revenue forecasting
- Comparable company calculations
- M&A modelling

## Purpose

This project demonstrates practical programming applications in:

- Investment banking
- Corporate finance
- Financial modelling
- Valuation
- M&A analysis
- Data analysis
- Financial visualization

## Disclaimer

This project is intended for educational, research, and portfolio purposes only.

It does not constitute investment advice, financial advice, or a recommendation to buy or sell any security.
