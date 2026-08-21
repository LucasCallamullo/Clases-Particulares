

import random
class Pais:
    def __init__(self, name, score, pos):
        self.name = name
        self.score = score
        self.id = pos
        self.points = 0
        self.goals_f = 0
        self.goals_c = 0

    def __str__(self):
        return f"{self.name} | Puntos: {self.points} | Goles_F: {self.goals_f} | Goles_C: {self.goals_c}"
    
    def get_goals_in_match(self):
        goals = random.randint(0, self.score)
        return goals
    
    def set_goals(self, goal_f, goal_c):
        self.goals_f += goal_f
        self.goals_c += goal_c
    
    def add_points(self, points):
        self.points += points
    