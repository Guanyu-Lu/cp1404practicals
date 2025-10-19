"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}
print(CODE_TO_NAME)
abbreviation_width=max(len(abbreviation) for abbreviation in CODE_TO_NAME.keys())
name_width=max(len(name) for name in CODE_TO_NAME.values())
for abbreviation,name in CODE_TO_NAME.items():
    print(f"{abbreviation:{abbreviation_width}} is {name:{name_width}}")
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
