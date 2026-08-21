from match import Match

class KnockoutStage:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.wins = 0

    def add_match(self, c1, c2):
        self.matches.append(Match(c1, c2))

    def play_all(self):
        winners = []
        print(f"--- {self.name} ---")
        for match in self.matches:
            country_win = match.play(knockout=True)
            winners.append(country_win)
            
        return winners