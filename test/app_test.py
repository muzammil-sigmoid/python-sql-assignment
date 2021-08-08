from unittest import TestCase
from src.app import App


class AppTest(TestCase):
    def setUp(self) -> None:
        self.app = App()

    def tearDown(self) -> None:
        self.app =None

    def test_initiation(self):
        self.assertIsNotNone(self.app.db)
        self.assertIsNone(self.app.cur)