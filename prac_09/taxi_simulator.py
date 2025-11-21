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
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                distance=float(input("Drive how far?"))
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.drive(distance)}")
                total_bill+=taxis[current_taxi].drive(distance)
                print(f"Bill to date: ${total_bill:.2f}")
        elif choice == "C":
            print("Taxis available:")
            for i,taxi in enumerate(taxis,0):
                print(f"{i} - {taxi}")
        chosen_taxi=int(input("Choose taxi:"))
        if chosen_taxi < 0 or chosen_taxi >= len(taxis):
            print("Invalid taxi choice.")
        else:
            current_taxi = taxis[chosen_taxi]
        print(f"Bill to date: ${total_bill:.2f}")


main()