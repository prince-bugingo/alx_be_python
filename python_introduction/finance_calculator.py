#User Input for Financial Details
income = input( "Enter your monthly income:" )
expenses = input( "Enter your monthly expenses:" )

#Calculate Monthly Savings:
monthly_savings = income - expenses

#Project Annual Savings:
annual_interest_rate = 0.05
annual_savings = monthly_savings * 12
annual_interest = annual_savings * annual_interest_rate
projected_savings = annual_savings * annual_interest

#Output Results:
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")