from urllib import request
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        players_file = request.urlopen(self._url)
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),       # name
                    parts[1].strip(),       # team
                    int(parts[3].strip()),  # goals
                    int(parts[4].strip())   # assists
                )

                players.append(player)

        return players
