from match import Match


class Group:
    def __init__(self, name):
        self.name = name
        self.countries = []
        self.fixture = []

    def add_country(self, pais):
        self.countries.append(pais)

    def make_fixture(self):
        self.fixture = [
            Match(self.countries[0], self.countries[1]),
            Match(self.countries[2], self.countries[3]),
            
            Match(self.countries[0], self.countries[2]),
            Match(self.countries[1], self.countries[3]),
            
            Match(self.countries[0], self.countries[3]),
            Match(self.countries[1], self.countries[2]),
        ]

    def play_next_match(self):
        if self.fixture:
            match = self.fixture.pop(0)
            match.play()

    def __str__(self):
        standings = sorted(
            self.countries, key=lambda c: (c.points, c.goals_f - c.goals_c), reverse=True
        )
        chain = f'{self.name}\n'
        for c in standings:
            chain += f"{c}\n"
        return chain
    
    def get_podium(self):
        standings = sorted(
            self.countries, key=lambda c: (c.points, c.goals_f - c.goals_c), reverse=True
        )
        return standings[0], standings[1]