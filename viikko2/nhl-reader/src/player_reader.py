import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        """Hakee NHL-raakadatan verkosta ja palauttaa listan Player-luokan olioita."""
        response = requests.get(self._url).json()

        all_players = []

        for player_dict in response:
            player = Player(player_dict)
            all_players.append(player)

        return all_players
