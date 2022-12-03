class TennisGame:
    def __init__(self, player1_name, player2_name):
        self._serve = player1_name
        self._returner = player2_name
        self._scores = {player1_name: 0, player2_name: 0}
        self._points_to_words_conversion = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

    def won_point(self, player_name):
        self._scores[player_name] += 1

    def get_score(self):
        winner = self._check_for_winner()
        if winner:
            return winner

        if self._score_difference() == 0:
            if self._player_score(self._serve) < 4:
                score = self._points_to_words_conversion[self._player_score(self._serve)] + "-All"
            else: score = "Deuce"

        elif max(self._scores.values()) > 3:

            if self._score_difference() == 1:
                score = f"Advantage {self._serve}"
            else:
                score = f"Advantage {self._returner}"
        else:
            score = f"{self._points_to_words_conversion[self._player_score(self._serve)]}-{self._points_to_words_conversion[self._player_score(self._returner)]}"

        return score

    def _player_score(self, player):
        return self._scores[player]

    def _score_difference(self):
        return self._scores[self._serve] - self._scores[self._returner]

    def _check_for_winner(self):
        template = "Win for "
        if self._score_difference() >= 2 and self._player_score(self._serve) > 3:
            return template + self._serve
        if self._score_difference() <= -2 and self._player_score(self._returner) > 3:
            return template + self._returner
        return None