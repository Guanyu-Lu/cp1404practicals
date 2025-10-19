COLOUR_INFORMATION_LOWER = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alicealue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff",
}
colour_name=input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"colour code for {colour_name} is {COLOUR_INFORMATION_LOWER[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter colour name: ").lower()
