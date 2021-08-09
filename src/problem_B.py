from src.problem import Problem
from src.excel import Excel
from datetime import date
import logging
log = logging.getLogger(__name__)


class ProblemB(Problem):
    def __init__(self,cur):
        super(ProblemB, self).__init__(cur)
        self.excel = Excel()

    # takes start_date and end_date as date object
    # returns the months difference between two dates
    def get_months_spent(self, start_date, end_date):
        return (end_date.year-start_date.year)*12 + end_date.month - start_date.month

    # returns total compensation
    def get_total_compensation(self,months_spent,  monthly_sal, commission):
        return months_spent * monthly_sal + commission


    def solve(self):
        column_names = ["Employee_Name", "Dept_Name", "Total_Compensation", "Months_spent"]
        log.info("fetching records")
        self.cur.execute("select emp.empno,emp.ename,jobhist.startdate,jobhist.enddate,jobhist.sal,jobhist.comm,dept.dname from emp join jobhist on emp.empno = jobhist.empno join dept on dept.deptno=emp.deptno;")
        temp_records = self.cur.fetchall()
        data = {}
        log.info("processing records")
        for row in temp_records:
            emp_no = row[0]
            emp_name = row[1]
            start_date = row[2]
            end_date = row[3] if row[3] is not None else date.today()
            monthly_sal = row[4]
            commission = 0 if row[5] is None else row[5]
            months_spent = self.get_months_spent(start_date,end_date)
            total_compensation = self.get_total_compensation(months_spent, monthly_sal, commission)
            department = row[6]
            # if there is some repeated data
            # if some employee appears twice than its compensation is compounded
            # else new record is added
            if emp_no in data:
                data[emp_no][2]+=total_compensation
                data[emp_no][3]+=months_spent
            else:
                data[emp_no] = [emp_name, department, total_compensation, months_spent]
        log.info("records processed")
        self.excel.save_index_as_key_data_as_value(column_names, data, "solutionB.xlsx")
        self.result = True












