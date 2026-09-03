# Model Assumptions

## Overview

This document summarizes the principal assumptions used by the Investment Banking Deal Analytics & Valuation Platform.

The assumptions are illustrative and are intended to demonstrate financial modelling techniques rather than represent forecasts for an actual company.

## Historical Financials

The historical company dataset contains five fiscal years of illustrative financial information.

The model uses:

- Revenue
- Cost of goods sold
- Operating expenses
- Depreciation and amortization
- Capital expenditures
- Change in net working capital
- Tax rate

The latest available historical period is used as the starting point for several valuation calculations.

## Revenue Forecast

The current revenue forecast uses:

**Annual revenue growth: 8%**

The growth assumption is applied consistently across the five-year forecast period.

The assumption is configurable within the forecasting module.

## DCF Assumptions

The current DCF implementation uses:

| Assumption | Value |
| --- | ---: |
| WACC | 9.0% |
| Terminal growth | 3.0% |
| Forecast period | 5 years |

The terminal growth rate must remain below the WACC for the Gordon Growth calculation to remain mathematically valid.

## Comparable Companies

The comparable-company analysis uses a synthetic peer group.

The principal valuation multiples are:

- EV / Revenue
- EV / EBITDA

Median peer multiples are used rather than simple averages to reduce the influence of extreme observations.

## Precedent Transactions

The precedent transactions dataset contains synthetic acquisition transactions.

The principal transaction multiples are:

- Transaction Value / Revenue
- Transaction Value / EBITDA

Median transaction multiples are used for the simplified valuation analysis.

## M&A Assumptions

The illustrative merger model uses:

| Assumption | Value |
| --- | ---: |
| Buyer net income | 500 |
| Target net income | 120 |
| Purchase price | 2,500 |
| Cash financing | 500 |
| Debt financing | 1,000 |
| Stock financing | 1,000 |
| Interest rate | 5.0% |
| Tax rate | 25.0% |
| Synergies | 40 |
| Buyer shares | 100 |
| New shares | 20 |

These values demonstrate the mechanics of a simplified accretion/dilution analysis.

## Sensitivity Analysis

The DCF sensitivity analysis varies:

### WACC

- 7.0%
- 8.0%
- 9.0%
- 10.0%
- 11.0%

### Terminal Growth

- 2.0%
- 2.5%
- 3.0%
- 3.5%
- 4.0%

The sensitivity matrix shows how enterprise value changes across these assumptions.

## Financial Units

The financial datasets use simplified currency units rather than a specific real-world reporting currency.

The project is intended to demonstrate financial modelling mechanics rather than produce a currency-specific valuation.

## Data Assumptions

All datasets are synthetic.

No confidential company, client, bank, or transaction information is required.

The comparable-company and precedent-transaction datasets are structured to resemble inputs that could be used in an investment banking valuation exercise.

## Model Simplifications

The current implementation intentionally simplifies several areas.

### Forecasting

Revenue is forecast using a constant growth rate rather than a detailed operational driver model.

### DCF

Forecast free cash flow is based on an illustrative growth approach rather than a fully integrated financial statement forecast.

### Comparable Companies

The peer group is small and synthetic.

### Precedent Transactions

The transaction sample is illustrative and does not include detailed transaction adjustments.

### M&A

The merger model uses simplified financing, interest, synergy, and share-count mechanics.

### Valuation Summary

The current valuation summary uses a simple average of selected valuation outputs.

## Sensitivity Interpretation

The sensitivity analysis should be interpreted as a scenario analysis rather than a probability distribution.

Each WACC and terminal-growth combination represents an alternative modelling assumption.

The analysis is intended to show valuation sensitivity rather than predict the probability of any specific scenario.

## Future Enhancements

A more advanced version could incorporate:

- Dynamic operating assumptions
- Detailed margin forecasts
- Explicit WACC construction
- Capital structure assumptions
- Debt schedules
- Detailed working capital modelling
- Tax schedules
- Scenario probabilities
- More extensive peer datasets
- Transaction-specific adjustments
- Detailed M&A financing mechanics

## Disclaimer

All assumptions are illustrative and synthetic.

The model is intended for educational, research, and portfolio purposes and should not be interpreted as investment advice or a professional valuation.
