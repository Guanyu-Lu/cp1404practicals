from prac_07.guitar import Guitar
import csv

FILENAME = "guitars.csv"
YEAR_WIDTH = 4

def main():
    """Run the program to display the guitars based on the file."""
    guitars = load_data()
    print("These are the guitars loaded from the file:")
    display_guitars(guitars)
    guitars= add_new_data(guitars)
    guitars.sort()
    print("\nHere are all guitars sorted by year (from oldest to newest):")
    display_guitars(guitars)
    save_data(guitars)
    print(f"{len(guitars)} guitars have been saved to {FILENAME} successfully.")

def load_data():
    """Load data from file and return a list."""
    guitars = []
    try:
        with open(FILENAME, 'r') as in_file:
            reader = csv.reader(in_file)
            for parts in reader:
                if len(parts) == 3:
                    guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
                    guitars.append(guitar)
    except FileNotFoundError:
        print(f"Sorry,{FILENAME} not found.")
    return guitars


def add_new_data(guitars):
    """Add new guitars to the list."""
    guitar_name = input("Name: ")
    while guitar_name.strip() != "":
        guitar_year = get_valid_input("Year: ", int)
        guitar_cost = get_valid_input("Cost: $", float)
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        print(f"{guitar_name} ({guitar_year}) : ${guitar_cost:,.2f} added.\n")
        guitar_name = input("Name: ")
    return guitars


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


def calculate_display_width(guitars):
    """Calculate the maximum widths needed for name and cost."""
    name_width = max(len(guitar.name) for guitar in guitars)
    maximum_cost= max(guitar.cost for guitar in guitars)
    cost_width=len(f"{maximum_cost:,.2f}")
    return cost_width, name_width


def display_guitars(guitars):
    """Display guitars information in list."""
    cost_width, name_width = calculate_display_width(guitars)
    print("... snip ...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:  {guitar.name:>{name_width}} ({guitar.year:{YEAR_WIDTH}}), "
              f"worth $ {guitar.cost:{cost_width},.2f}{vintage_string}")


def save_data(guitars):
    """Save data from guitars."""
    outfile = open("guitars.csv", "w")
    for guitar in guitars:
        print(",".join([guitar.name,str(guitar.year),str(guitar.cost)]), file=outfile)


main()