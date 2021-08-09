
# base class  for
# all problem class inherits this class
# initially the result is false
# after successfully solving the problem
# child class will set result value to True
class Problem:
    def __init__(self, cur):
        self.cur = cur
        self.result = False

    def get_result(self):
        return self.result