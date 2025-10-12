"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = get_incomes()
    print_report(incomes)

def get_incomes():
    """Get monthly incomes based on number of months from user input."""
    incomes = []
    number_of_months = get_valid_months()
    for month in range(1, number_of_months + 1):
        income = get_valid_incomes(month)
        incomes.append(income)
    return incomes

def get_valid_months():
    """Get valid number of months based on user input."""
    is_integer = False
    while not is_integer:
        try:
            number_of_months = int(input("How many months? "))
            if number_of_months >=0:
                is_integer = True
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter an integer.")
    return number_of_months

def get_valid_incomes(month):
    """Get valid incomes based on user input."""
    is_float = False
    while not is_float:
        try:
            income = float(input(f"Enter income for month {month} : "))
            if income >=0:
                is_float = True
            else:
                print("Please enter a positive float.")
        except ValueError:
            print("Please enter a float.")
    return income

def print_report(incomes):
    """Print income report including monthly income and total income"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()