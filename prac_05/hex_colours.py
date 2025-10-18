COLOUR_INFORMATION = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Apricot": "#fbceb1",
    "Aqua": "#00ffff",
}
colour_name=input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"colour code for {colour_name} is {COLOUR_INFORMATION[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter colour name: ").title()
