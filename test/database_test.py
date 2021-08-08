from unittest import TestCase
from src.database import Database

class DatabaseTest(TestCase):

    def setUp(self) -> None:
        self.db = Database()

    def tearDown(self) -> None:
        self.db = None

    def test_connection_uri(self):
        self.assertTrue('dbname' in self.db.uri)
        self.assertTrue('user' in self.db.uri)
        self.assertTrue('password' in self.db.uri)

