"""
Programming_languages
Estimate: 15 minutes
Actual:   9 minutes
"""

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance.
               name: string, name of the programming language
               typing: string, type checking method of the programming language
               reflection: bool, reflection status of the programming language(True=Can reflection, False=Not reflection)
               year: integer, first release year the programming language
               """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language uses dynamic typing."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a f-string representation of the language object."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"