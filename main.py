#Asking Monthly allowance
monthly_allowance = float(input("What is your monthly allowance? : $"))

# Expenses
expense_1 = float(input("How much do you pay monthly for rent? : $"))
expense_2 = float(input("How much do you spend on groceries per month : $"))
expense_3 = float(input("How much do you spend on transportation per month : $"))
expense_4 = float(input("How much do you spend on entertainment per month : $"))

total_expenses = expense_1 + expense_2 + expense_3 + expense_4
balance = monthly_allowance - total_expenses

# Results 
print("Your monthly allowance is: $",monthly_allowance)

print("Total expenses: $",round(total_expenses, 2))

print("Your remaining balance: $", balance)