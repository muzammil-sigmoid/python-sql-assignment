from unittest import TestCase
from src.problem import Problem


class ProblemTest(TestCase):
    def setUp(self) -> None:
        self.problem = Problem("cur")

    def tearDown(self) -> None:
        self.problem = None

    def test_get_result(self):
        self.assertEqual(self.problem.get_result(), False)
