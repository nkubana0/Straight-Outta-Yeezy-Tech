from main import ValueAtRisk

# Create a ValueAtRisk instance
mypos = ValueAtRisk('USD', 11)

# Import historical data for assets and currencies
mypos.asset_import('MartyCorp', 'USD', (90.0, 94.0, 93.0, 91.0, 90.0, 100.0, 104.0, 103.0, 101.0, 99.0, 100.0))
mypos.asset_import('XYZ', 'EUR', (57.0, 54.5, 57.0, 55.0, 57.0, 55.5, 57.0, 56.0, 57.0, 55.5, 57.0))
mypos.curr_import('EUR', (0.90, 0.87, 0.90, 0.88, 0.94, 0.91, 0.91, 0.99, 0.90, 0.92, 0.92))

# Buy some assets
mypos.buy('MartyCorp', 100)
mypos.buy('XYZ', 20)

# Test VAR calculation for individual assets
var_marty = mypos.get_var('MartyCorp', 'Total', 0.80)
var_xyz = mypos.get_var('XYZ', 'Total', 0.80)

print("1-Day Value at Risk for 100 MartyCorp - Equities with a confidence level of 80% is", var_marty, "USD.")
print("1-Day Value at Risk for 20 XYZ - Equities with a confidence level of 80% is", var_xyz, "EUR.")

# Test VAR calculation for the whole portfolio
var_total = mypos.get_var('ALL', 'Total', 0.80)
var_equity = mypos.get_var('ALL', 'Equity', 0.80)
var_forex = mypos.get_var('ALL', 'Forex', 0.80)

print("1-Day Total Value at Risk for the portfolio with a confidence level of 80% is", var_total, "USD.")
print("1-Day Equity Value at Risk for the portfolio with a confidence level of 80% is", var_equity, "USD.")
print("1-Day Forex Value at Risk for the portfolio with a confidence level of 80% is", var_forex, "EUR.")