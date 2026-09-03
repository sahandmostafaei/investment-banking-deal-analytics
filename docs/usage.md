# Usage Guide

## Overview

The Investment Banking Deal Analytics & Valuation Platform is designed to execute an end-to-end financial analysis workflow from historical company data through valuation, transaction analysis, visualization, and Excel reporting.

## Project Inputs

The main input datasets are located in the `data/` directory:

- `company_financials.csv`
- `comparable_companies.csv`
- `precedent_transactions.csv`

These datasets provide the inputs for the financial analysis and valuation modules.

## Main Application

The primary application entry point is:

`main.py`

The application coordinates the complete analytical workflow.

## Workflow

The application performs the following steps:

### 1. Load Financial Data

Historical company financial statements are loaded from the CSV dataset.

### 2. Calculate Financial Metrics

The financial analysis module calculates:

- Gross profit
- EBITDA
- EBIT
- NOPAT
- Unlevered free cash flow

### 3. Generate Revenue Forecast

The forecasting module generates a five-year revenue forecast using the configured growth assumption.

### 4. Perform DCF Valuation

Forecast cash flows are discounted using the selected WACC and terminal growth assumptions.

The resulting DCF analysis produces:

- Present values of forecast cash flows
- Terminal value
- Present value of terminal value
- Enterprise value

### 5. Analyze Comparable Companies

Comparable companies are analyzed using:

- EV / Revenue
- EV / EBITDA

Median multiples are calculated and applied to target-company financial metrics.

### 6. Analyze Precedent Transactions

Historical transactions are analyzed using:

- Transaction Value / Revenue
- Transaction Value / EBITDA

Median transaction multiples are calculated.

### 7. Generate DCF Sensitivity Analysis

The model evaluates enterprise value across multiple combinations of:

- WACC
- Terminal growth

### 8. Build Valuation Summary

The DCF, comparable-company, and precedent-transaction valuation outputs are combined into a consolidated summary.

### 9. Perform M&A Analysis

The merger model estimates:

- Pro forma net income
- Pro forma shares
- Buyer EPS
- Pro forma EPS
- Accretion/dilution

### 10. Generate Visualizations

The application generates financial charts and stores them in the `figures/` directory.

### 11. Export Results to Excel

The final analytical datasets are exported to:

`figures/valuation_analysis.xlsx`

## Python Modules

The main analytical modules are:

`src/financials.py`

Historical financial analysis.

`src/forecasting.py`

Revenue forecasting.

`src/dcf.py`

Discounted Cash Flow valuation.

`src/comparables.py`

Comparable companies analysis.

`src/precedents.py`

Precedent transactions analysis.

`src/merger_model.py`

M&A accretion/dilution modelling.

`src/sensitivity.py`

DCF sensitivity analysis.

`src/valuation_summary.py`

Consolidated valuation analysis.

`src/visualization.py`

Financial visualization.

`src/export.py`

Excel reporting.

`src/utils.py`

Output formatting utilities.

## Outputs

The main generated outputs are stored in `figures/`.

Expected outputs include:

- `revenue_forecast.png`
- `dcf_sensitivity.png`
- `valuation_analysis.xlsx`

The Excel workbook contains separate worksheets for the primary financial and valuation datasets.

## Testing

The project uses pytest for automated testing.

The test suite covers the primary analytical modules and validates expected calculation behaviour.

## Development

Project dependencies are defined in:

`requirements.txt`

Project metadata is defined in:

`pyproject.toml`

A Makefile provides simplified project commands for installation, testing, execution, and cleanup.

## Model Assumptions

The project uses illustrative assumptions for:

- Revenue growth
- WACC
- Terminal growth
- Interest rates
- Tax rates
- Transaction synergies
- Financing structure

These assumptions are intended to demonstrate the mechanics of financial modelling rather than provide a real investment recommendation.

## Extending the Project

The platform can be extended by adding:

- Additional financial datasets
- More detailed operating forecasts
- Additional valuation methodologies
- Capital structure modelling
- Debt schedules
- Scenario analysis
- Additional M&A transaction mechanics
- More advanced visualization
- Additional Excel reporting functionality

The modular architecture is intended to make these extensions straightforward.

## Disclaimer

This project is an educational and portfolio demonstration.

The data is synthetic and the assumptions are illustrative. The platform should not be considered professional investment-banking software, a professional valuation report, or investment advice.
