import random
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
NUMBERS_PER_PICK = 6
def main():
    """Get number of quick picks and print quick picks"""
    number_of_quick_picks = get_valid_picks()
    print_quick_picks(number_of_quick_picks)

def get_integer(prompt):
    is_integer=False
    while not is_integer:
        try:
            number_of_quick_picks=int(input(prompt))
            is_integer=True
        except ValueError:
            print("Please enter a integer.")
    return number_of_quick_picks

def get_valid_picks():
    number_of_quick_picks = get_integer("How many quick picks? ")
    while number_of_quick_picks <= 0:
        print("Please enter a positive integer")
        number_of_quick_picks=get_integer("How many quick picks? ")
    return number_of_quick_picks

def generate_pick_number(numbers):
    random_number=random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    while random_number in numbers:
        random_number=random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    numbers.append(random_number)
    return numbers

def print_quick_picks(number_of_quick_picks):
    for line in range(number_of_quick_picks):
        quick_picks = generate_picks()
        print(" ".join(f"{pick:2}" for pick in quick_picks))

def generate_picks():
    numbers=[]
    for pick in range(NUMBERS_PER_PICK):
        generate_pick_number(numbers)
    numbers.sort()
    return numbers

main()