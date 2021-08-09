import pandas as pd
from res.config import config
import os

import logging
log = logging.getLogger(__name__)


class Excel:
    def __init__(self):
        self.filepath = config["out_folder_path"]

    # takes column names as list and records as list of tuples
    # takes filename with extension
    # creates dataframe and save it to configured folder
    def save(self, column_names, records,filename):
        try:
            df = pd.DataFrame(records, columns=column_names)
            df.to_excel(os.path.join(self.filepath,filename),index=False)
            log.info(f"{filename} saved as excel")
        except Exception as err:
            log.error(err)
            raise Exception("Failed to save file")

    # takes column names as list and records as dictionary with first column as keys and
    # other columns as values in a list
    # takes filename with extension
    # creates dataframe and save it to configured folder
    def save_index_as_key_data_as_value(self,column_names,records,filename):
        try:
            df = pd.DataFrame.from_dict(records, orient="index", columns=column_names)
            df.index.name = "Employee_Number"
            df.to_excel(os.path.join(self.filepath,filename))
            log.info(f"{filename} saved as excel")
        except Exception as err:
            log.error(err.args)
            raise Exception("Failed to save file")

    # takes filename with extension
    # returns a tuple int the form (columns i list, records as list of tuples)
    def get_data_from_xlsx(self,filename):
        df = pd.read_excel(os.path.join(self.filepath,filename), index_col=None)
        log.info("read  the file.."+filename)
        return list(df.columns), df.to_records(index=False)

    # creates dataframe from xlsx file aqnd returns it
    def get_df_from_xlsx(self,filename):
        df = pd.read_excel(os.path.join(self.filepath, filename), index_col=None)
        return df

    # returns dataframe
    # takes columns list and list of tuples as data
    def get_df_from_columns_and_tuples(self,columns,tuples):
        return pd.DataFrame(tuples,columns=columns)

    # takes dataframe
    # save it as excel and ignores index column
    def save_df(self, df, filename):
        df.to_excel(os.path.join(self.filepath,filename),index=False)






