"""
guitar_test
Estimate: 10 minutes
Actual:   6 minutes
"""

from prac_06.guitar import Guitar
CURRENT_YEAR=2025


def main():
    """Test Guitar class methods (get_age and is_vintage)."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar= Guitar("Another Guitar", 2013, 1500)
    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()