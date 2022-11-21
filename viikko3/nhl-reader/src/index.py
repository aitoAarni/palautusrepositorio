import requests
from player import Player

class PlayerReader:
    def __init__(self, url) -> None:
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(player) for player in response]


class PlayerStats:
    def __init__(self, players) -> None:
        self.players = players

    def top_sorted_by_nationality(self, nat: str) -> list:
        players = list(filter(lambda x: x.nationality == nat, self.players))
        players.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"


    reader = PlayerReader(url)

    stats = reader.get_players()
    print(stats)
    players = PlayerStats(stats)
    players = players.top_sorted_by_nationality("FIN")


    for player in players:

        print(player)

if __name__ == "__main__":
    main()
