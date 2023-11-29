class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.points = 0

    def add_point(self):
        self.points += 1

    def get_points_string(self):
        if self.points == 0:
            return "Love"
        elif self.points == 1:
            return "Fifteen"
        elif self.points == 2:
            return "Thirty"
        elif self.points == 3:
            return "Forty"
        return self.points