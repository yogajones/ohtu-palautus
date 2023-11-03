import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_search_finds_player(self):
        find_semenko = self.stats.search("Semenko")
        self.assertEqual(find_semenko.name, "Semenko")


    def test_search_doesnt_find_player(self):
        find_humpty_dumpty = self.stats.search("Humpty Dumpty")
        self.assertIsNone(find_humpty_dumpty)

    
    def test_team_returns_team(self):
        return_edm = self.stats.team("EDM")
        self.assertIsNotNone(return_edm)


    def test_top_returns_top3(self):
        top3 = self.stats.top(3)
        self.assertEqual(len(top3), 3)