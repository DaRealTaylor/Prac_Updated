# Electricity bill estimator
# Enter cents per kWh: 35
# Enter daily use in kWh: 4.5
# Enter number of billing days: 90
# Estimated bill: $141.75

billing_days = 90
cents_per_kWh = int(input("Input kWh usage"))
daily_use = int(input("Input daily use"))
total = cents_per_kWh * daily_use * billing_days / 100
print("$", total)

# to be continued