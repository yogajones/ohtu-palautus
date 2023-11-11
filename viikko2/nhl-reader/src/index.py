import requests
from player import Player

def main():
    # tallenna raakadata
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # luo lista kaikista pelaajista
    all_players = []

    for player_dict in response:
        player= Player(player_dict)
        all_players.append(player)

    # tulosta suomalaiset pelaajat
    FILTER_NATIONALITY = "FIN"
    
    print(f"Players from {FILTER_NATIONALITY}:")
    players_filtered = filter(lambda player: player.nationality == FILTER_NATIONALITY, all_players)
    players_sorted_by_points = sorted(players_filtered, key=lambda player: player.points, reverse=True)
    for player in players_sorted_by_points:
        print(player)

if __name__ == "__main__":
    main()
