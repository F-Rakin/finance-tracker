# Expenses (Float numbers)

def expenses():
    """
    Asks user for different expenses in a month

    :return: Stores Sum(expenses)
    """

    rent = float(input("How much do you pay monthly for rent? : $"))
    groceries = float(input("How much do you spend on groceries per month : $"))
    transportation = float(input("How much do you spend on transportation per month : $"))
    entertainment = float(input("How much do you spend on entertainment per month : $"))

    total_expenses = rent + groceries + transportation + entertainment   # Adds up all the expenses
    return total_expenses

# Results 

def results(monthly_allowance, total_expenses):
    """
    Prints results based on inputted values
    
    :return: Allowance, Total expense and Balance
    """
    balance = monthly_allowance - total_expenses  # Calculates remaining balance

    print("Your monthly allowance is: $",monthly_allowance)
    print("Total expenses: $",round(total_expenses, 2))
    print("Your remaining balance: $",round(balance, 2))

    return balance

# Conditional statements depending on spendings

def conditions(balance):
    """
    Gives a conditional statement based on spendings
    
    :return: A text message
    """
    if balance > 0:
        print("Congrats! You have more money to spend.")  # Will show this message if you underspend
    else: 
        print("You have spent too much!!! Plan your spendings ") # Will show this message if you overspend

def main():
    monthly_allowance = float(input("What is your monthly allowance? : $"))
    calculate_expenses = expenses()
    show_remaining_balance = results(monthly_allowance, calculate_expenses)
    conditions(show_remaining_balance)

main()