from unittest import TestCase
from src.excel import Excel


class ExcelTest(TestCase):

    def setUp(self) -> None:
        self.excel = Excel()

    def tearDown(self) -> None:
        self.excel = None

    def test_file_path_is_set(self):
        self.assertIsNotNone(self.excel.filepath)


