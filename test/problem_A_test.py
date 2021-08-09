from unittest import TestCase
from src.problem_A import ProblemA


class ProblemATest(TestCase):

    def setUp(self) -> None:
        self.probA = ProblemA("cur")

    def tearDown(self) -> None:
        self.probA = None

    def test_get_column_names(self):
        columns = self.probA.get_column_names()
        self.assertTrue("Employee Number" in columns)
        self.assertTrue("Employee Name" in columns)
        self.assertTrue("Assigned Manager"in columns)
