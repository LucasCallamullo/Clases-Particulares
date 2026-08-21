import random


class Match:
    def __init__(self, country1, country2):
        self.country1 = country1
        self.country2 = country2
        self.played = False

    def play(self, knockout=False):
        goals1 = self.country1.get_goals_in_match()
        goals2 = self.country2.get_goals_in_match()
        print()
        print(f"{self.country1.name} {goals1} - {goals2} {self.country2.name}")
        

        country_win = None
        if goals1 > goals2:
            self.country1.add_points(3)
            country_win = self.country1
            
        elif goals1 == goals2:
            self.country1.add_points(1)
            self.country2.add_points(1)
            
            if knockout:
                country_win = self.penalties()
            
        else:
            self.country2.add_points(3)
            country_win = self.country2

        self.country1.set_goals(goal_f=goals1, goal_c=goals2)
        self.country2.set_goals(goal_f=goals2, goal_c=goals1)
        self.played = True
        
        return country_win
        
    def penalties(self):
        while (True):
            penals1 = random.randint(0, 5)
            penals2 = random.randint(0, 5)
            if penals1 != penals2:
                break
            
        print(f"Penales: {self.country1.name} {penals1} - {penals2} {self.country2.name}")
        return self.country1 if penals1 > penals2 else self.country2