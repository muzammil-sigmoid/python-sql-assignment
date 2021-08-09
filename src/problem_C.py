from src.problem import Problem
from src.excel import Excel

import logging
log = logging.getLogger(__name__)


class ProblemC(Problem):

    def __init__(self, cur):
        super(ProblemC, self).__init__(cur)
        self.excel = Excel()

    # creates table in database
    # takes list of column names
    def create_table(self, column_names):
        try:
            log.info("creating table")
            self.cur.execute('DROP TABLE if exists compensation')
            self.cur.execute(f'create table compensation ({column_names[0]} int,'
                             f' {column_names[1]} varchar(256),'
                             f' {column_names[2]} varchar(256),'
                             f' {column_names[3]} numeric,'
                             f' {column_names[4]} int);')
        except Exception as err:
            log.error(err.args)
            raise Exception("Creation of table failed")

    # provided list of tuples
    # inserts every row in database sequentially
    def insert_rows(self,records):
        try:
            # if there is no records then error is raised
            if len(records) == 0:
                raise Exception("zero length")
            log.info("inserting rows")
            for row in records:
                self.cur.execute(f"INSERT INTO COMPENSATION VALUES {row};")
        except Exception as err:
            log.error(err.args)
            raise Exception("Insertion in table Failed")

    def solve(self):
        column_names, records = self.excel.get_data_from_xlsx("solutionB.xlsx")
        self.create_table(column_names)
        self.insert_rows(records)
        self.result=True







