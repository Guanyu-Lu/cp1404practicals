"""
Module"Guitars!"
Estimate: 20 minutes
Actual:   21 minutes
"""

from prac_06.guitar import Guitar
YEAR_WIDTH=4


def main():
    """Run the Guitar program."""
    print("My guitars!")
    guitars=get_valid_data()
    print()
    if len(guitars)==0:
        print("No guitars!")
    else:
        cost_width, name_width = calculate_display_width(guitars)
        display_guitars(cost_width, guitars, name_width)


def calculate_display_width(guitars):
    """Calculate the maximum widths needed for name and cost."""
    name_width = max(len(guitar.name) for guitar in guitars)
    maximum_cost= max(guitar.cost for guitar in guitars)
    cost_width=len(f"{maximum_cost:,.2f}")
    return cost_width, name_width


def get_valid_data():
    """Get valid data including name, year and cost for Guitars."""
    guitars=[]
    guitar_name = input("Name: ")
    while len(guitar_name) != 0:
        guitar_year = get_valid_input("Year: ",int)
        guitar_cost = get_valid_input("Cost: $",float)
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:,.2f} added.\n")
        guitar_name = input("Name: ")
    return guitars


def display_guitars(cost_width, guitars, name_width):
    """Display guitars information in list."""
    print("... snip ...")
    print()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year:{YEAR_WIDTH}}), "
              f"worth $ {guitar.cost:{cost_width},.2f}{vintage_string}")


def get_valid_input(prompt,number_type):
    """Get a valid input from the user."""
    is_valid=False
    while not is_valid:
        try:
            number=number_type(input(prompt))
            is_valid=True
        except ValueError:
            print("Invalid input. Try again.")
    return number


main()