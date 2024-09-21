#User Input for Financial Details
income = input( "Enter your monthly income:" )
expenses = input( "Enter your monthly expenses:" )

#Calculate Monthly Savings:
monthly_savings = income - expenses

#Project Annual Savings:
rate = 0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#Output Results:
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")