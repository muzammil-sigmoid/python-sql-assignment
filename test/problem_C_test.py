from unittest import TestCase
from src.problem_C import ProblemC

class ProblemCTest(TestCase):
    def setUp(self) -> None:
        self.probC = ProblemC("cur")

    def tearDown(self) -> None:
        self.probC = None

    def test_insert_rows_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.probC.insert_rows([],[])
        self.assertTrue('Insertion in table ' in str(context.exception))

    def test_create_table_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.probC.create_table([])
        self.assertTrue('failed' in str(context.exception))