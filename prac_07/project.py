"""
Languages
Estimate: 20 minutes
Actual:    minutes
"""
class Project:
    def __init__(self,name,start_date,priority,estimate_cost,completed_percentage):
        self.name=name
        self.start_date=start_date
        self.priority=priority
        self.estimate_cost=estimate_cost
        self.completed_percentage=completed_percentage

    def __str__(self):
        formatted_date = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start:{formatted_date}, "
                f"priority {self.priority}, estimate: ${self.estimate_cost:.2f}, "
                f"completed_percentage: {self.completed_percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

