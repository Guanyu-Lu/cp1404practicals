"""
Languages
Estimate: 20 minutes
Actual:   20 minutes
"""
class Project:
    """Represent a Project object."""

    def __init__(self,name,start_date,priority,estimate_cost,completed_percentage):
        """Initialise a Project instance.
        name: str,name of project.
        start_date: datetime.date object,start date of project.
        priority: int,priority of project.
        estimate_cost: float,estimated cost of project.
        completed_percentage: int,completed percentage of project.
        """
        self.name=name
        self.start_date=start_date
        self.priority=priority
        self.estimate_cost=estimate_cost
        self.completed_percentage=completed_percentage

    def __str__(self):
        """Return a formatted string representation of the Project."""
        formatted_date = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start:{formatted_date}, "
                f"priority {self.priority}, estimate: ${self.estimate_cost:.2f}, "
                f"completed_percentage: {self.completed_percentage}%")

    def __lt__(self, other):
        """Define comparison for sorting based on project priority"""
        return self.priority < other.priority

    def get_start_date_for_sort(self):
        """Return the start_date attribute for use as a sort key."""
        return self.start_date