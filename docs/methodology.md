# Financial Modelling Methodology

## 1. Financial Statement Analysis

Historical company financials are used to derive operating and cash-flow metrics.

### Gross Profit

Gross profit is calculated as:

Gross Profit = Revenue - COGS

### EBITDA

EBITDA is calculated as:

EBITDA = Gross Profit - Operating Expenses

### EBIT

EBIT is calculated as:

EBIT = EBITDA - Depreciation & Amortization

### NOPAT

Net Operating Profit After Tax is calculated as:

NOPAT = EBIT × (1 - Tax Rate)

### Unlevered Free Cash Flow

Unlevered free cash flow is calculated as:

UFCF = NOPAT + D&A - Capex - Change in NWC

These metrics provide the operating cash-flow foundation for valuation.

---

## 2. Revenue Forecasting

The forecasting module applies a constant annual growth assumption to the latest historical revenue.

The forecast follows:

Forecast Revenue = Previous Revenue × (1 + Growth Rate)

The current implementation uses an illustrative 8% annual growth assumption.

The growth assumption is configurable within the Python forecasting function.

---

## 3. Discounted Cash Flow Valuation

The DCF model estimates enterprise value by discounting forecast unlevered free cash flows to their present value.

The present value of each forecast cash flow is calculated using the applicable WACC.

The terminal value uses the Gordon Growth Method:

Terminal Value = Final Year FCF × (1 + g) / (WACC - g)

where:

- FCF = final forecast unlevered free cash flow
- g = terminal growth rate
- WACC = weighted average cost of capital

Enterprise value is then calculated as:

Enterprise Value = PV of Forecast FCFs + PV of Terminal Value

The model assumes:

WACC > Terminal Growth Rate

to maintain a mathematically valid terminal value.

---

## 4. Comparable Companies Analysis

Comparable companies valuation uses market-based trading multiples.

The primary multiples used are:

- Enterprise Value / Revenue
- Enterprise Value / EBITDA

For each comparable company:

EV / Revenue = Enterprise Value / Revenue

EV / EBITDA = Enterprise Value / EBITDA

The median multiple is then applied to the target company's corresponding financial metric.

For example:

Implied EV = Target EBITDA × Median EV / EBITDA

Using the median rather than the mean reduces the influence of extreme observations.

---

## 5. Precedent Transactions

Precedent transactions valuation applies acquisition transaction multiples to the target company.

The primary transaction multiples are:

- Transaction Value / Revenue
- Transaction Value / EBITDA

For each transaction:

Transaction Multiple = Deal Value / Target Financial Metric

Median transaction multiples are then applied to the target company's financial metrics.

This approach provides an acquisition-market-based valuation reference.

---

## 6. Valuation Triangulation

The platform combines multiple valuation methodologies:

- DCF
- Comparable Companies
- Precedent Transactions

Each method provides a different perspective.

### DCF

Focuses on the company's expected future cash generation.

### Comparable Companies

Reflects how similar publicly traded companies are valued by the market.

### Precedent Transactions

Reflects valuation levels observed in historical acquisitions.

The current implementation calculates a simple average across selected enterprise-value estimates.

In professional investment banking models, valuation conclusions may instead use analyst-selected ranges, weighting methodologies, or transaction-specific judgment.

---

## 7. DCF Sensitivity Analysis

DCF valuation is sensitive to assumptions regarding:

- WACC
- Terminal growth

The sensitivity module evaluates enterprise value across combinations of these assumptions.

A lower WACC generally increases valuation because future cash flows are discounted at a lower rate.

A higher terminal growth rate generally increases terminal value, provided that the growth rate remains below WACC.

The sensitivity matrix allows users to evaluate the robustness of the valuation under alternative assumptions.

---

## 8. M&A Accretion / Dilution

The merger model estimates the effect of an acquisition on buyer earnings per share.

The simplified model incorporates:

- Buyer net income
- Target net income
- Transaction synergies
- Debt financing
- Interest expense
- Tax effects
- Buyer shares
- New shares issued

After-tax financing cost is calculated as:

After-Tax Interest = Interest Expense × (1 - Tax Rate)

Pro forma net income is then estimated as:

Pro Forma Net Income = Buyer Net Income + Target Net Income + Synergies - After-Tax Interest

Pro forma EPS is:

Pro Forma EPS = Pro Forma Net Income / Pro Forma Shares

Accretion/dilution is:

Accretion / Dilution = Pro Forma EPS / Buyer EPS - 1

A positive percentage indicates accretion.

A negative percentage indicates dilution.

---

## 9. Excel Reporting

Analytical outputs are exported programmatically to an Excel workbook.

The workbook contains:

- Historical financials
- Revenue forecast
- Comparable companies
- Precedent transactions
- DCF sensitivity analysis

This demonstrates integration between Python-based financial analysis and spreadsheet-based financial reporting.

---

## 10. Software Architecture

The project separates analytical functionality into independent Python modules.

This allows:

- Individual functions to be tested
- Financial assumptions to be changed
- Analytical components to be reused
- Additional valuation methods to be added
- Outputs to be integrated into reporting workflows

The main execution flow is coordinated through `main.py`.

---

## 11. Data Assumptions

The datasets included in the repository are synthetic.

They are designed to provide realistic
