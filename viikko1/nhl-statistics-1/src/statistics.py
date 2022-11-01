
def sort_by(player, category):
    if not category or category.value == 1:
        return player.points
    if category.value == 2:
        return player.goals
    if category.value == 3:
        return player.assists



class Statistics:
    def __init__(self, playerReader):
        reader = playerReader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_category=None):
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=lambda x: sort_by(x, sort_category)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
