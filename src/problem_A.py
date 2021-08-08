from src.problem import Problem
from src.excel import Excel
import logging
log = logging.getLogger(__name__)


class ProblemA(Problem):
    def __init__(self, cur):
        super(ProblemA, self).__init__(cur)
        self.excel = Excel()

    def get_column_names(self):
        return ["Employee Number", "Employee Name", "Assigned Manager"]

    def solve(self):
        self.cur.execute("select emp1.empno,emp1.ename,emp2.ename as manager from emp as emp1 left join emp as emp2 on emp2.empno=emp1.mgr;")
        log.info("fetched records")
        records = self.cur.fetchall()
        column_names = self.get_column_names()
        log.info('saving to excel')
        self.excel.save(column_names, records,"solutionA.xlsx")
        self.result = True



