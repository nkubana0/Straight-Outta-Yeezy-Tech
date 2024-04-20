# Value at Risk (VAR) Calculator

This is a simple Python program to calculate the Value at Risk (VAR) for equity positions based on historical data.

## Description

Value at Risk (VAR) is a measure used in finance to quantify the potential loss on an investment or portfolio over a specific time period with a certain confidence level. This project implements a VAR calculator using the historical simulation approach.

## Features

- Import historical data for equities and currencies.
- Calculate the past relative shifts of equity rates.
- Maintain equity positions by buying and selling.
- Calculate VAR for individual equities or the whole portfolio.
- Consider different risk classes (Total, Equity, Forex) and confidence levels.

## Usage

1. **Initialize the portfolio**:
    - Create a `ValueAtRisk` instance with the base currency and history length.
    - Import historical data for equities and currencies using `asset_import` and `curr_import` methods.

2. **Maintain Equity Position**:
    - Buy and sell equities using the `buy` and `sell` methods.

3. **Calculate VAR**:
    - Use the `get_var` method to calculate VAR for individual equities or the whole portfolio.
    - Specify the asset name, risk class ('Total', 'Equity', 'Forex'), and confidence level.

## Example

```python
from value_at_risk import ValueAtRisk

# Create a ValueAtRisk instance with base currency historical rates
base_rates = [1.0] * 11  # Assuming the base currency rates are all 1.0
mypos = ValueAtRisk('USD', 11, base_rates)

# Import historical data for assets and currencies
mypos.asset_import('MartyCorp', 'USD', (90.0, 94.0, 93.0, 91.0, 90.0, 100.0, 104.0, 103.0, 101.0, 99.0, 100.0))
mypos.asset_import('XYZ', 'EUR', (57.0, 54.5, 57.0, 55.0, 57.0, 55.5, 57.0, 56.0, 57.0, 55.5, 57.0))
mypos.curr_import('EUR', (0.90, 0.87, 0.90, 0.88, 0.94, 0.91, 0.91, 0.99, 0.90, 0.92, 0.92))

# Buy some assets
mypos.buy('MartyCorp', 100)
mypos.buy('XYZ', 20)

# Calculate VAR for individual assets
var_marty = mypos.get_var('MartyCorp', 'Total', 0.80)
var_xyz = mypos.get_var('XYZ', 'Total', 0.80)

# Calculate VAR for the whole portfolio
var_total = mypos.get_var('ALL', 'Total', 0.80)
var_equity = mypos.get_var('ALL', 'Equity', 0.80)
var_forex = mypos.get_var('ALL', 'Forex', 0.80)
