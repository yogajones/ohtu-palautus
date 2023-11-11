from player_reader import PlayerReader
from player_stats import PlayerStats


def main():
    """Tulostaa suomalaiset NHL-pelaajat pistejärjestyksessä."""

    # luo pelaajalistan
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    # rajaa pelaajat suomalaisiin ja järjestää pisteiden mukaan
    filter_nationality = "FIN"
    players = stats.top_scorers_by_nationality(filter_nationality)

    # tulostaa rajatun ja järjestetyn pelaajalistan muotoiltuna
    print(f"\nPlayers from {filter_nationality}:\n")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
