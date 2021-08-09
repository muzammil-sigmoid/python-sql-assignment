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

    # returns the cursor
    def get_db_cursor(self):
        self.cur = self.db.connect()

    # receives ques object and ques_type as 'A','B','C','D'....
    def solve_problem(self, ques, ques_type):
        try:
            log.info("solving problem "+ques_type)
            problem = ques(self.cur)
            problem.solve()
            if problem.get_result() is False:
                raise Exception("Failed to Solve problem "+ques_type)
            log.info(f"Problem {ques_type} solved.")
        except Exception as err:
            log.error("for problem " + ques_type)
            log.error(err.args)
            raise Exception(f"Fail to solve {ques_type}")

    # the driver function which calls each problem
    # sequential run
    # i.e. fails and stops if any question fails
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





