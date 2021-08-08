from src.problem import Problem
from src.excel import Excel
import logging
log = logging.getLogger(__name__)

class ProblemD(Problem):

    def __init__(self,cur):
        super(ProblemD,self).__init__(cur)
        self.excel = Excel()

    def solve(self):
        df = self.excel.get_df_from_xlsx("solutionB.xlsx")
        self.cur.execute("select * from dept")
        records_dept = self.cur.fetchall()
        df_dept  = self.excel.get_df_from_columns_and_tuples(["Dept_No","Dept_Name","loc"],records_dept)
        log.info("merging tables")
        df_merged = df.merge(df_dept,on="Dept_Name",how="inner")
        df_dept_compensation = df_merged[['Dept_No','Dept_Name','Total_Compensation']].groupby(by="Dept_No").\
            agg({'Dept_Name':'max','Total_Compensation':"sum"})
        log.info("saving to excel")
        self.excel.save_df(df_dept_compensation,"solutionsD.xlsx")
        self.result = True


