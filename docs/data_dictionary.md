# Data Dictionary

## Overview

The project uses three synthetic CSV datasets as inputs to the financial analysis and valuation workflow.

All data is illustrative and created for educational and portfolio purposes.

## 1. Company Financials

File:

`data/company_financials.csv`

This dataset contains historical operating and cash-flow information for the target company.

| Field | Description | Unit |
| --- | --- | --- |
| `year` | Fiscal year | Year |
| `revenue` | Total company revenue | Currency units |
| `cogs` | Cost of goods sold | Currency units |
| `operating_expenses` | Operating expenses excluding COGS and D&A | Currency units |
| `da` | Depreciation and amortization | Currency units |
| `capex` | Capital expenditure | Currency units |
| `change_nwc` | Change in net working capital | Currency units |
| `tax_rate` | Assumed tax rate | Decimal |

### Derived Metrics

The financial analysis module derives:

- Gross profit
- EBITDA
- EBIT
- NOPAT
- Unlevered free cash flow

## 2. Comparable Companies

File:

`data/comparable_companies.csv`

This dataset contains simplified financial and valuation information for peer companies.

| Field | Description | Unit |
| --- | --- | --- |
| `company` | Comparable-company name | Text |
| `revenue` | Company revenue | Currency units |
| `ebitda` | Company EBITDA | Currency units |
| `enterprise_value` | Enterprise value | Currency units |
| `net_debt` | Net debt | Currency units |
| `market_cap` | Equity market capitalization | Currency units |

### Derived Metrics

The comparable-company module calculates:

- EV / Revenue
- EV / EBITDA
- Simplified equity valuation multiple

Median peer multiples are subsequently calculated.

## 3. Precedent Transactions

File:

`data/precedent_transactions.csv`

This dataset contains simplified historical acquisition information.

| Field | Description | Unit |
| --- | --- | --- |
| `transaction` | Transaction name | Text |
| `deal_value` | Transaction or acquisition value | Currency units |
| `target_revenue` | Target-company revenue | Currency units |
| `target_ebitda` | Target-company EBITDA | Currency units |

### Derived Metrics

The precedent transactions module calculates:

- Transaction Value / Revenue
- Transaction Value / EBITDA

Median transaction multiples are then calculated.

## Data Flow

The datasets feed different parts of the analytical workflow.

### Company Financials

`company_financials.csv`

→ Financial statement analysis

→ Historical EBITDA and EBIT

→ NOPAT

→ Unlevered free cash flow

→ DCF valuation

### Comparable Companies

`comparable_companies.csv`

→ Trading multiples

→ Median peer multiples

→ Implied target valuation

### Precedent Transactions

`precedent_transactions.csv`

→ Transaction multiples

→ Median transaction multiples

→ Implied target valuation

## Data Quality Considerations

The project uses structured CSV files so that analytical functions can operate consistently on tabular data.

In a production environment, additional validation would normally be required for:

- Missing values
- Duplicate records
- Invalid financial periods
- Negative or inconsistent financial metrics
- Currency differences
- Accounting-policy differences
- Outliers
- Data-source reliability

## Synthetic Data

The datasets are synthetic.

They are not intended to represent the actual financial performance or valuation of any real company or transaction.

This approach allows the project to demonstrate financial modelling techniques without relying on confidential or proprietary information.

## Extension Opportunities

The data layer could be expanded to support:

- Additional historical periods
- Multiple target companies
- Larger comparable-company universes
- Additional transaction records
- Industry classifications
- Geographic classifications
- Market data
- Capital structure information
- Detailed financial statements

## Disclaimer

All data in this repository is illustrative and intended for educational and portfolio purposes.
