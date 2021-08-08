from unittest import TestCase
from src.problem_D import ProblemD


class ProblemDTest(TestCase):
    def setUp(self) -> None:
        self.probD = ProblemD("cur")

    def tearDown(self) -> None:
        self.probD = None

    def test_excel_object(self):
        self.assertIsNotNone(self.probD.excel)

