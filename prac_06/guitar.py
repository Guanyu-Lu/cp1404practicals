"""
guitar_test
Estimate: 10 minutes
Actual:   8 minutes
"""

CURRENT_YEAR=2025
class Guitar:
    def __init__(self,name="", year=0, cost=0):
        """Initialise a Guitar instance.
        name: string, name of the guitar
        year: integer, The year of guitar making
        cost: float, the cost of the guitar
        """
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name}({self.year}): ${self.cost:,2f}"

    def get_age(self):
        """Return the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage(more than or equal to 50 years)."""
        return self.get_age()>=50
