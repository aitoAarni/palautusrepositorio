import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )


    def test_constructor_works(self):
        Reader = PlayerReaderStub()
        players = Reader.get_players()
        print(self.statistics._players)
        print(players)
        self.assertEqual(len(self.statistics._players), len(players))

    def test_search_returns_right_player(self):
        player = self.statistics.search('Kurri')
        self.assertEqual(player.name, 'Kurri')

    def test_searh_returns_none_if_no_player_matching(self):
        player = self.statistics.search('kamboodia')
        self.assertIsNone(player)

    def test_team_method_finds_right_players(self):
        players = self.statistics.team('EDM')
        self.assertEqual(len(players), 3)
        
    def test_top_players_method_works(self):
        t = self.statistics.top(3)
        self.assertTupleEqual((
            t[0].name,
            t[1].name,
            t[2].name,
            len(t)
        ), (
            'Gretzky',
            'Lemieux',
            'Yzerman',
            4
        )
)