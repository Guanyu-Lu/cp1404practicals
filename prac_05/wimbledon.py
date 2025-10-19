"""
Word Occurrences
Estimate: 35 minutes
Actual:   25 minutes
"""
import csv
FILENAME="wimbledon.csv"
COUNTRY_INDEX=1
CHAMPION_INDEX=2

def main():
    """Display the list of championship wins and their countries based on wimbledon.csv."""
    champion_to_wins, countries =read_data(FILENAME)
    display_champion_details(champion_to_wins)
    display_countries_details(countries)


def read_data(filename):
    """Read and extract the data."""
    champion_to_wins = {}
    countries = set()
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            champion_to_wins[record[CHAMPION_INDEX]] = champion_to_wins.get(record[CHAMPION_INDEX], 0)+1
            countries.add(record[COUNTRY_INDEX])
    return champion_to_wins,countries


def display_champion_details(champion_to_wins):
    """Display all the champions and their number of victories."""
    print("Wimbledon Champions:")
    for champion,wins in champion_to_wins.items():
        print(f"{champion} {wins}")


def display_countries_details(countries):
    """Display the total number of countries that have won the championship."""
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()