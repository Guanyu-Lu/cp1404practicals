import random
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBERS_PER_PICK = 6
def main():
    """Get number of quick picks and print quick picks"""
    number_of_quick_picks = get_valid_picks()
    print_quick_picks(number_of_quick_picks)

def get_integer(prompt):
    """Get an integer instead of a string or float."""
    is_integer=False
    while not is_integer:
        try:
            number_of_quick_picks=int(input(prompt))
            is_integer=True
        except ValueError:
            print("Please enter a integer.")
    return number_of_quick_picks

def get_valid_picks():
    """Get number of quick picks and ensure it is a positive integer."""
    number_of_quick_picks = get_integer("How many quick picks? ")
    while number_of_quick_picks <= 0:
        print("Please enter a positive integer")
        number_of_quick_picks=get_integer("How many quick picks? ")
    return number_of_quick_picks

def generate_pick_number(numbers):
    """Generate a unique random number and add to the list."""
    random_number=random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    while random_number in numbers:
        random_number=random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    numbers.append(random_number)
    return numbers

def generate_picks():
    """Generate a list of random picks."""
    numbers=[]
    for pick in range(NUMBERS_PER_PICK):
        generate_pick_number(numbers)
    numbers.sort()
    return numbers

def print_quick_picks(number_of_quick_picks):
    """Print the specified number of quick picks, and align the format."""
    for line in range(number_of_quick_picks):
        quick_picks = generate_picks()
        print(" ".join(f"{pick:2}" for pick in quick_picks))

main()