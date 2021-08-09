from unittest import TestCase
from src.problem_B import ProblemB
from datetime import date


class ProblemBTest(TestCase):
    def setUp(self) -> None:
        self.probB = ProblemB("cur")

    def tearDown(self) -> None:
        self.probB = None

    def test_get_months_spent(self):
        self.assertEqual(self.probB.get_months_spent(date(2021,5,17),date(2021,6,16)),1)
        self.assertEqual(self.probB.get_months_spent(date(2020, 5, 17), date(2021, 6, 16)), 13)
        self.assertEqual(self.probB.get_months_spent(date(2019, 5, 17), date(2021, 6, 16)), 25)
        self.assertEqual(self.probB.get_months_spent(date(2021, 5, 17), date(2021, 5, 20)), 0)
        self.assertEqual(self.probB.get_months_spent(date(2018, 5, 17), date(2021, 6, 16)), 37)
        self.assertEqual(self.probB.get_months_spent(date(2017, 5, 17), date(2021, 6, 16)), 49)

    def test_total_compensation(self):
        self.assertEqual(self.probB.get_total_compensation(10,12,34),154)
        self.assertEqual(self.probB.get_total_compensation(20, 12, 34), 274)
        self.assertEqual(self.probB.get_total_compensation(10, 1, 34), 44)
        self.assertEqual(self.probB.get_total_compensation(10, 12, 0), 120)
        self.assertEqual(self.probB.get_total_compensation(10, 11, 0), 110)