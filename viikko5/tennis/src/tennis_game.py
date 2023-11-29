from player import Player


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._player1 = Player(player1_name)
        self._player2 = Player(player2_name)

    def _point_difference(self):
        return self._player1.points - self._player2.points

    def won_point(self, player_name):
        if player_name == self._player1.name:
            self._player1.add_point()
        else:
            self._player2.add_point()

    def _even_points(self):
        if self._player1.points < 3:
            return self._player1.get_points_string() + "-All"
        return "Deuce"

    def _both_under_4_points(self):
        return self._player1.get_points_string() + "-" + \
            self._player2.get_points_string()

    def _advantage_or_win(self):
        if self._point_difference() == 1:
            return "Advantage player1"
        elif self._point_difference() == -1:
            return "Advantage player2"
        elif self._point_difference() >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_score(self):
        if self._point_difference() == 0:
            return self._even_points()

        if self._player1.points < 4 and self._player2.points < 4:
            return self._both_under_4_points()

        return self._advantage_or_win()
