# Testing Strategy

## Overview

The project uses `pytest` to validate the core financial modelling and analytical functions.

The testing strategy focuses on verifying that individual modules produce expected outputs for controlled inputs.

## Testing Objectives

The test suite is intended to:

- Validate core financial calculations.
- Detect unintended changes to analytical logic.
- Verify expected output structures.
- Check important financial relationships.
- Provide a basic regression-testing framework.
- Improve confidence when extending the project.

## Test Organization

Tests are stored in the `tests/` directory.

The test suite is organized by analytical module.

### Financial Analysis

`test_financials.py`

Tests calculations including:

- Gross profit
- EBITDA
- EBIT
- NOPAT
- Unlevered free cash flow

### Forecasting

`test_forecasting.py`

Tests the revenue forecasting functionality and expected forecast output.

### DCF

`test_dcf.py`

Tests that the DCF model produces an enterprise value and that the resulting valuation is positive for valid inputs.

### Comparable Companies

`test_comparables.py`

Tests:

- Trading multiple calculations
- Median multiple calculations
- Target-company valuation outputs

### Precedent Transactions

`test_precedents.py`

Tests:

- Transaction multiple calculations
- Median transaction multiples

### M&A Model

`test_merger_model.py`

Tests the simplified merger model and its principal outputs, including:

- Pro forma net income
- Pro forma EPS
- Accretion/dilution

### Sensitivity Analysis

`test_sensitivity.py`

Tests the dimensions and valid outputs of the DCF sensitivity matrix.

### Valuation Summary

`test_valuation_summary.py`

Tests the aggregation of DCF, comparable-company, and precedent-transaction valuation outputs.

### Excel Export

`test_export.py`

Tests that the valuation workbook is successfully created at the specified output path.

### Utilities

`test_utils.py`

Tests formatting functions for:

- Currency values
- Percentage values

## Test Design

The tests generally use small controlled datasets rather than the full project datasets.

This makes individual functions easier to validate and reduces dependencies between tests.

For example, the financial metric tests construct a small pandas DataFrame with known inputs and compare the calculated outputs against expected values.

## Regression Testing

Tests provide a basic regression-testing layer.

When analytical functions are modified, the test suite can help identify whether existing expected behaviour has changed.

This is particularly useful for financial models because small changes in calculations can propagate into valuation outputs.

## CI Integration

The repository includes a GitHub Actions workflow configured to run the pytest suite on pushes and pull requests targeting the `main` branch.

The CI workflow installs the project dependencies and executes the test suite automatically.

## Future Testing Improvements

A more advanced testing framework could include:

- Edge-case testing
- Input validation tests
- Missing-data tests
- Invalid-assumption tests
- Property-based testing
- Numerical tolerance checks
- Integration tests
- End-to-end pipeline tests
- Coverage measurement
- Financial-model reconciliation tests

## Testing Philosophy

The objective is not to test every line of code independently.

The objective is to validate the key analytical behaviour of the financial modelling system while keeping the test suite understandable and maintainable.

## Disclaimer

The testing framework validates software behaviour against synthetic and illustrative inputs.

Passing tests do not imply that the underlying financial assumptions are appropriate for a real investment decision or professional valuation.
