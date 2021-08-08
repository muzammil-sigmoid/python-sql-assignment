import logging

from src.database import Database
from src.problem_A import ProblemA
from src.problem_B import ProblemB
from src.problem_C import ProblemC
from src.problem_D import ProblemD

log = logging.getLogger(__name__)


class App:
    def __init__(self):
        self.cur = None
        self.db = Database()

    def get_db_cursor(self):
        self.cur = self.db.connect()

    def solve_problem(self,ques,ques_type):
        try:
            log.info("solving problem "+ques_type)
            problem = ques(self.cur)
            problem.solve()
            if problem.get_result() is False:
                raise Exception("Failed to Solve problem "+ques_type)
            log.info(f"Problem {ques_type} solved.")
        except Exception as err:
            log.error("for problem " + ques_type)
            log.error(err.args[0])

    def solve(self):
        try:
            self.get_db_cursor()
            self.solve_problem(ProblemA, "A")
            self.solve_problem(ProblemB, "B")
            self.solve_problem(ProblemC, "C")
            self.solve_problem(ProblemD, "D")
            self.db.close()
        except Exception as err:
            log.error(err.args[0])
        finally:
            log.info("Closing App")





