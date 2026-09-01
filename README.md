```markdown
# Investment Banking Deal Analytics

A Python-based investment banking analytics and valuation platform.

## What It Does

This project automates several core investment banking and corporate finance workflows:

- Financial statement analysis
- Revenue forecasting
- DCF valuation
- Comparable company analysis
- Precedent transaction analysis
- DCF sensitivity analysis
- M&A accretion/dilution analysis
- Financial visualization

## Technology

Python | pandas | NumPy | SciPy | Matplotlib | pytest

## Architecture

```text
Financial Data
      |
      v
Financial Statement Analysis
      |
      v
Revenue Forecast
      |
      +------------------+
      |                  |
      v                  v
     DCF            Comparable Companies
      |                  |
      v                  v
DCF Sensitivity    Precedent Transactions
      |                  |
      +---------+--------+
                |
                v
          Valuation Analysis
                |
                v
        M&A Accretion/Dilution
Project Structure
investment-banking-deal-analytics/
│
├── data/
│   ├── company_financials.csv
│   ├── comparable_companies.csv
│   └── precedent_transactions.csv
│
├── figures/
│   ├── revenue_forecast.png
│   └── dcf_sensitivity.png
│
├── src/
│   ├── financials.py
│   ├── forecasting.py
│   ├── dcf.py
│   ├── comparables.py
│   ├── precedents.py
│   ├── merger_model.py
│   ├── sensitivity.py
│   ├── visualization.py
│   └── utils.py
│
├── tests/
│   ├── test_dcf.py
│   ├── test_financials.py
│   ├── test_forecasting.py
│   ├── test_comparables.py
│   └── test_merger_model.py
│
├── main.py
├── PROJECT.md
├── README.md
├── requirements.txt
└── .gitignore
Key Outputs
The platform produces:
Historical financial metrics
Revenue forecasts
Enterprise value from DCF
Trading comparable multiples
Precedent transaction multiples
DCF sensitivity tables
M&A accretion/dilution estimates
Revenue forecast visualization
DCF sensitivity visualization
Disclaimer
This project is for educational and portfolio purposes and does not constitute investment advice.
