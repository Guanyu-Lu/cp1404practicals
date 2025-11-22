class Band:
    """Band class for storing details of a band and its musicians."""

    def __init__(self, name):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musicians_strings = [str(musician) for musician in self.musicians ]
        return f"{self.name} ({', '.join(musicians_strings)})"

    def __repr__(self):
        """Return a string representation of a band, showing the variables."""
        return  str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the result of playing music by all musicians."""
        if not self.musicians:
            return f"{self.name} needs an musician!"
        else:
            play_results=[]
            for musician in self.musicians:
                play_results.append(musician.play())
            return "\n".join(play_results)
