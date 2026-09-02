# Investment Banking Deal Analytics & Valuation Platform

A Python-based investment banking analytics platform for financial analysis, valuation, M&A modelling, financial visualization, Excel reporting, and automated testing.

## Overview

This project simulates a simplified investment banking transaction analysis workflow using Python.

The platform processes company financial data and applies several core investment banking and corporate finance techniques:

- Financial statement analysis
- EBITDA and EBIT calculation
- Unlevered free cash flow analysis
- Revenue forecasting
- Discounted Cash Flow (DCF) valuation
- Comparable companies analysis
- Precedent transactions analysis
- Enterprise value estimation
- Valuation sensitivity analysis
- M&A accretion/dilution analysis
- Financial visualization
- Excel valuation reporting
- Automated testing

The project is designed to demonstrate practical programming and quantitative finance skills relevant to investment banking, valuation, corporate finance, and financial analytics.

## Technology Stack

- Python
- pandas
- NumPy
- SciPy
- Matplotlib
- openpyxl
- pytest

## Project Workflow

The platform follows a simplified investment banking valuation workflow:

Company / Transaction Data  
↓  
Financial Statement Analysis  
↓  
Revenue Forecast  
↓  
DCF Valuation  
↓  
Comparable Companies  
↓  
Precedent Transactions  
↓  
Enterprise Value  
↓  
Equity Value Analysis  
↓  
Accretion / Dilution  
↓  
Sensitivity Analysis  
↓  
Visualization & Excel Reporting

## Financial Analysis

Historical financial statements are loaded from CSV data and transformed into analytical metrics.

The model calculates:

- Revenue
- Gross profit
- EBITDA
- EBIT
- NOPAT
- Unlevered Free Cash Flow

The calculations provide the foundation for the subsequent valuation analysis.

## Revenue Forecasting

The forecasting module generates a five-year revenue projection using a configurable annual growth rate.

The forecast is designed to demonstrate:

- Time-series financial modelling
- Forecast assumptions
- Iterative calculations
- pandas DataFrame construction
- Integration of historical and projected financial data

The default model uses an 8% annual revenue growth assumption.

## DCF Valuation

The project implements a simplified Discounted Cash Flow valuation model.

The DCF analysis includes:

- Forecast free cash flows
- WACC assumption
- Terminal growth assumption
- Present value of forecast cash flows
- Terminal value
- Present value of terminal value
- Enterprise value

The model uses a Gordon Growth terminal value approach.

## Comparable Companies Analysis

The comparable companies module analyzes a peer group using publicly available-style financial metrics.

The analysis calculates:

- Enterprise Value / Revenue
- Enterprise Value / EBITDA
- Simplified equity valuation multiple

Median trading multiples are then applied to target-company financial metrics to estimate implied valuation.

This demonstrates the programming structure behind a simplified trading comparables analysis.

## Precedent Transactions

The precedent transactions module analyzes historical acquisition transactions.

For each transaction, the model calculates:

- Transaction Value / Revenue
- Transaction Value / EBITDA

Median transaction multiples are calculated and applied to the target company's EBITDA and revenue to estimate an implied enterprise value.

This provides a simplified precedent transactions valuation framework.

## Valuation Summary

The valuation summary module combines multiple valuation approaches.

The platform compares:

- DCF enterprise value
- Comparable companies enterprise value
- Precedent transactions enterprise value

An average enterprise value is calculated to provide a simple valuation reference point across methodologies.

## DCF Sensitivity Analysis

The sensitivity analysis module evaluates how DCF enterprise value changes under different assumptions.

The model varies:

- WACC
- Terminal growth rate

The result is a two-dimensional valuation sensitivity table.

This demonstrates how investment banking valuation models can be structured to evaluate the impact of key assumptions.

## M&A Accretion / Dilution

The M&A module implements a simplified merger model.

The model considers:

- Buyer net income
- Target net income
- Purchase price
- Cash financing
- Debt financing
- Stock financing
- Interest expense
- Tax effects
- Transaction synergies
- Buyer shares
- New shares issued

The model calculates:

- Pro forma net income
- Pro forma shares
- Buyer EPS
- Pro forma EPS
- Accretion / dilution

A positive result represents accretion, while a negative result represents dilution.

## Excel Valuation Workbook

The project generates an Excel valuation workbook containing:

- Historical financials
- Revenue forecast
- Comparable companies
- Precedent transactions
- DCF sensitivity analysis

Generated workbook:

figures/valuation_analysis.xlsx

The workbook is created programmatically using pandas and openpyxl.

## Visualizations

The project generates financial analysis charts using Matplotlib.

Current visual outputs include:

- Historical and forecast revenue
- DCF sensitivity visualization

Generated figures are stored in the `figures/` directory.

## Project Structure

investment-banking-deal-analytics/

    data/
        company_financials.csv
        comparable_companies.csv
        precedent_transactions.csv

    src/
        __init__.py
        financials.py
        forecasting.py
        dcf.py
        comparables.py
        precedents.py
        merger_model.py
        sensitivity.py
        valuation_summary.py
        export.py
        visualization.py
        utils.py

    figures/
        revenue_forecast.png
        dcf_sensitivity.png
        valuation_analysis.xlsx

    tests/
        test_dcf.py
        test_financials.py
        test_forecasting.py
        test_comparables.py
        test_precedents.py
        test_merger_model.py
        test_sensitivity.py
        test_valuation_summary.py
        test_export.py
        test_utils.py

    main.py
    requirements.txt
    .gitignore
    PROJECT.md
    README.md

## Modules

### `financials.py`

Loads historical financial statements and calculates core financial metrics.

### `forecasting.py`

Generates forward revenue projections based on configurable growth assumptions.

### `dcf.py`

Calculates discounted cash flow valuation and terminal value.

### `comparables.py`

Calculates trading multiples and applies peer valuation multiples to the target company.

### `precedents.py`

Calculates precedent transaction multiples and derives implied valuation.

### `merger_model.py`

Calculates simplified M&A pro forma earnings and accretion/dilution.

### `sensitivity.py`

Generates a DCF sensitivity matrix across WACC and terminal growth assumptions.

### `valuation_summary.py`

Combines valuation methodologies into a consolidated valuation summary.

### `export.py`

Exports analytical outputs into an Excel valuation workbook.

### `visualization.py`

Creates financial analysis charts using Matplotlib.

### `utils.py`

Provides reusable formatting functions for financial outputs.

## Testing

The project includes a pytest-based automated test suite covering the main analytical modules.

Tests cover:

- Financial metric calculations
- DCF valuation
- Revenue forecasting
- Comparable companies
- Precedent transactions
- M&A modelling
- DCF sensitivity analysis
- Valuation summaries
- Excel export
- Financial formatting utilities

The test suite is designed to provide basic validation of the analytical functions and improve code reliability.

## Key Skills Demonstrated

### Programming

- Python
- Object-oriented and functional programming concepts
- Modular code architecture
- Reusable functions
- Data processing
- File I/O
- Automated testing

### Financial Analysis

- Financial statement analysis
- EBITDA and EBIT analysis
- Free cash flow modelling
- Revenue forecasting
- Enterprise valuation
- Trading comparables
- Precedent transactions

### Investment Banking

- DCF valuation
- Valuation sensitivity analysis
- M&A modelling
- Accretion/dilution analysis
- Transaction analysis
- Excel-based financial reporting

### Quantitative & Data Skills

- pandas
- NumPy
- Matplotlib
- Numerical calculations
- Scenario analysis
- Structured financial datasets

## Purpose

This project was developed as a portfolio demonstration of programming, financial modelling, valuation, and quantitative analysis skills relevant to investment banking and corporate finance.

It is particularly intended to demonstrate the ability to translate financial concepts into reusable Python-based analytical workflows.

## Disclaimer

This project is an educational and portfolio demonstration.

The financial data is synthetic and the valuation assumptions are illustrative. The models are simplified implementations and should not be considered investment advice, professional valuation reports, or production investment banking models.
