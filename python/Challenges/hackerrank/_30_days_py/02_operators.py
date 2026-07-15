def solve(meal_cost, tip_percent, tax_percent):
    meal_cost = float(meal_cost)
    tip_percent = float(tip_percent)
    tax_percent = float(tax_percent)

    tax = meal_cost * tip_percent / 100 + meal_cost * tax_percent / 100
    total = meal_cost + tax
    print(round(total))

# Get user input
meal_cost = input()
tip_percent = input()
tax_percent = input()

# Call the solve function with the provided inputs
solve(meal_cost, tip_percent, tax_percent)
