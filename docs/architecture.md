# Software Architecture

## Overview

The Investment Banking Deal Analytics & Valuation Platform follows a modular architecture in which financial analysis, forecasting, valuation, transaction modelling, visualization, and reporting are separated into independent Python modules.

The architecture is designed to make individual analytical components reusable and testable.

## High-Level Architecture

The system follows this workflow:

Input Data  
→ Data Processing  
→ Financial Analysis  
→ Forecasting  
→ Valuation  
→ Transaction Analysis  
→ Sensitivity Analysis  
→ Visualization  
→ Excel Reporting

## Data Layer

The `data/` directory contains the input datasets used by the analytical modules.

Current datasets include:

- `company_financials.csv`
- `comparable_companies.csv`
- `precedent_transactions.csv`

The datasets are loaded using pandas.

## Analytical Layer

The `src/` directory contains the core financial and analytical logic.

### Financial Analysis

`financials.py`

Responsibilities:

- Load historical financial data
- Calculate gross profit
- Calculate EBITDA
- Calculate EBIT
- Calculate NOPAT
- Calculate unlevered free cash flow

### Forecasting

`forecasting.py`

Responsibilities:

- Identify the latest historical revenue
- Apply growth assumptions
- Generate forward revenue projections
- Return forecast data as a pandas DataFrame

### DCF Valuation

`dcf.py`

Responsibilities:

- Discount forecast cash flows
- Calculate terminal value
- Discount terminal value
- Calculate enterprise value

### Comparable Companies

`comparables.py`

Responsibilities:

- Load comparable-company data
- Calculate trading multiples
- Calculate median multiples
- Apply multiples to target-company financial metrics

### Precedent Transactions

`precedents.py`

Responsibilities:

- Load transaction data
- Calculate transaction multiples
- Calculate median transaction multiples

### M&A Modelling

`merger_model.py`

Responsibilities:

- Calculate financing-related interest expense
- Apply tax effects
- Incorporate transaction synergies
- Calculate pro forma net income
- Calculate pro forma shares
- Calculate pro forma EPS
- Calculate accretion/dilution

### Sensitivity Analysis

`sensitivity.py`

Responsibilities:

- Iterate across WACC assumptions
- Iterate across terminal growth assumptions
- Calculate DCF enterprise value for each scenario
- Return a two-dimensional sensitivity matrix

### Valuation Summary

`valuation_summary.py`

Responsibilities:

- Combine valuation outputs
- Compare valuation methodologies
- Calculate a consolidated enterprise-value estimate

## Reporting Layer

### Excel Export

`export.py`

The reporting module exports analytical outputs to an Excel workbook.

The workbook contains separate worksheets for:

- Financials
- Forecast
- Comparables
- Precedents
- DCF Sensitivity

The module uses pandas and openpyxl.

## Visualization Layer

`visualization.py`

The visualization module produces financial charts using Matplotlib.

Current visualizations include:

- Historical versus forecast revenue
- DCF sensitivity analysis

Outputs are stored in the `figures/` directory.

## Utility Layer

`utils.py`

Contains reusable formatting functions for:

- Currency values
- Percentages

Keeping formatting logic separate from analytical logic reduces duplication across the project.

## Application Entry Point

`main.py`

The main application coordinates the analytical workflow.

It:

1. Loads historical financials.
2. Calculates financial metrics.
3. Generates a revenue forecast.
4. Calculates DCF valuation.
5. Performs comparable companies analysis.
6. Performs precedent transactions analysis.
7. Generates DCF sensitivity analysis.
8. Builds a valuation summary.
9. Performs M&A accretion/dilution analysis.
10. Generates financial visualizations.
11. Exports analytical results to Excel.

The individual calculations remain inside their respective modules rather than being implemented entirely inside `main.py`.

## Testing Layer

The `tests/` directory contains pytest-based tests for the analytical modules.

Testing is organized around individual functions and modules.

This allows calculations to be validated independently rather than relying only on the complete application workflow.

## Configuration

Project-level Python metadata is defined in:

`pyproject.toml`

Runtime dependencies are listed in:

`requirements.txt`

Code-quality tooling is configured through:

`.pre-commit-config.yaml`

## Repository Infrastructure

The repository also includes:

- GitHub Actions configuration
- CODEOWNERS
- MIT License
- Contribution guidelines
- Security policy
- Citation metadata
- Makefile

These files provide standard software-project infrastructure around the financial analytics code.

## Design Principles

The project follows several basic software-engineering principles:

### Modularity

Financial calculations are separated into focused modules.

### Reusability

Core calculations are implemented as functions that can be reused with different inputs and assumptions.

### Testability

Analytical functions are tested independently using pytest.

### Separation of Concerns

Data loading, financial calculations, visualization, reporting, and application orchestration are separated.

### Extensibility

Additional valuation methods, financial datasets, forecasting assumptions, and transaction models can be added without redesigning the entire application.

## Current Scope

The architecture is intentionally lightweight.

It is designed as an educational and portfolio implementation rather than a production investment-banking platform.

The project demonstrates how financial modelling concepts can be translated into a structured Python application.
