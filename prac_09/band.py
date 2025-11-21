class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_strings = [str(musician) for musician in self.musicians ]
        return f"{self.name} ({', '.join(musicians_strings)})"

    def __repr__(self):
        return  str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        if not self.musicians:
            return f"{self.name} needs an musician!"
        else:
            play_results=[]
            for musician in self.musicians:
                play_results.append(musician.play())
            return "\n".join(play_results)
