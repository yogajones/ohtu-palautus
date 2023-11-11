from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, filter_nationality: str):
        """Rajaa pelaajat kansalaisuuden mukaan ja palauttaa pelaajat pistejärjestyksessä."""
        players_filtered = filter(
            lambda player: player.nationality == filter_nationality, self.reader.get_players())
        players_sorted_by_points = sorted(
            players_filtered, key=lambda player: player.points, reverse=True)
        return players_sorted_by_points
