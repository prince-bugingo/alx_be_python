#User Input for Financial Details
monthly_income = input( "Enter your monthly income:" )
monthly_expenses = input( "Enter your total monthly expenses:" )

#Calculate Monthly Savings:
monthly_savings = float(monthly_income) - float(monthly_expenses)

#Project Annual Savings:
annual_interest_rate = 0.05
annual_savings = monthly_savings * 12

annual_interest = annual_savings * annual_interest_rate
projected_savings = round(annual_savings * annual_interest)

#Output Results:
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest, is: {projected_savings}")
