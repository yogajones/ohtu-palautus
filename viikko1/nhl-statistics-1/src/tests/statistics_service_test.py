import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),    # 16
            Player("Lemieux", "PIT", 45, 54),   # 99
            Player("Kurri",   "EDM", 37, 53),   # 90
            Player("Yzerman", "DET", 42, 56),   # 98
            Player("Gretzky", "EDM", 35, 89)    # 124
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


    def test_top_returns_top3_point_getters_by_default(self):
        top3 = self.stats.top(3)
        self.assertEqual(top3[0].name, "Gretzky")
        self.assertEqual(top3[1].name, "Lemieux")
        self.assertEqual(top3[2].name, "Yzerman")


    def test_top_returns_top3_point_getters(self):
        top3 = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top3[0].name, "Gretzky")
        self.assertEqual(top3[1].name, "Lemieux")
        self.assertEqual(top3[2].name, "Yzerman")

    def test_top_returns_top3_goal_makers(self):
        top3 = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top3[0].name, "Lemieux")
        self.assertEqual(top3[1].name, "Yzerman")
        self.assertEqual(top3[2].name, "Kurri")

    def test_top_returns_top3_assisters(self):
        top3 = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top3[0].name, "Gretzky")
        self.assertEqual(top3[1].name, "Yzerman")
        self.assertEqual(top3[2].name, "Lemieux")