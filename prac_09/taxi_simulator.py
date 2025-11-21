from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU="q)uit, c)hoose taxi, d)rive"
def main():
    total_bill=None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    choice=input("{MENU}\n>>>").upper()
    while choice != "Q":
        if choice == "D":
            if current_taxi = None:
                print("You need to choose a taxi before you can drive")
            else:
                distance=float(input("Drive how far?"))
                print(f"Your Prius trip cost you ${taxis[current_taxi].drive(distance)}")
                total_bill+=taxis[current_taxi].drive(distance)
                print(f"Bill to date: ${total_bill:.2f}")

