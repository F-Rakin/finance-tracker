def expenses():
    """
    Asks user for different expenses in a month

    :return: Stores Sum(expenses)
    """
    while True:
        try:
            rent = float(input("How much do you pay monthly for rent? : $"))
            groceries = float(input("How much do you spend on groceries per month : $"))
            transportation = float(input("How much do you spend on transportation per month : $"))
            entertainment = float(input("How much do you spend on entertainment per month : $"))
            break

        except: ValueError
        print("Please enter a proper number")
        
    total_expenses = rent + groceries + transportation + entertainment   # Adds up all the expenses
    return total_expenses

expenses()