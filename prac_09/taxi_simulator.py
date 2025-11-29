from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Run a taxi simulator program."""
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    choice = input(f"{MENU}\n>>>").upper()
    while choice != "Q":
        if choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill = drive_taxi(current_taxi, total_bill)
        elif choice == "C":
            current_taxi = choose_taxi(current_taxi, taxis)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(f"{MENU}\n>>>").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def drive_taxi(current_taxi,current_bill):
    """Ask for distance, drive, and update bill."""
    distance = get_valid_number("Drive how far?",float)
    if distance <0:
        print("Invalid number.")
        return current_bill
    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    return current_bill+trip_cost

def choose_taxi(current_taxi,taxis):
    """Display available taxis and allow user to choose one."""
    print("Taxis available:")
    display_taxis(taxis)
    chosen_taxi = get_valid_number("Choose taxi:",int)
    if chosen_taxi < 0 or chosen_taxi >= len(taxis):
        print("Invalid taxi choice.")
    else:
        current_taxi = taxis[chosen_taxi]
    return current_taxi

def display_taxis(taxis):
    """Display the list of taxis with their indices."""
    for i, taxi in enumerate(taxis, 0):
        print(f"{i} - {taxi}")

def get_valid_number(prompt,number_type):
    """Get a valid number from the user."""
    is_valid=False
    number=0 #Set the initial value to 0
    while not is_valid:
        try:
            number=number_type(input(prompt))
            is_valid=True
        except ValueError:
            print("Invalid input. Try again.")
    return number

main()