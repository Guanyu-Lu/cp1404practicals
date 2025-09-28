"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Run the temperature conversion program based on user choice."""
    print(MENU)
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = get_choice()
    print("Thank you.")

def get_choice():
    """Get and return menu choice from user."""
    return input(">>> ").upper()

def convert_celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)

main()