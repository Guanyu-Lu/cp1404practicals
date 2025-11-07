from prac_07.guitar import Guitar
def main():
    """Run the program to display the guitars based on the file."""
    guitars = read_data()
    print_data(guitars)


def read_data():
    """Read data from file and return a list."""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    return guitars


def print_data(guitars):
    """Print data from guitars."""
    for guitar in guitars:
        print(guitar)


main()