import pandas as pd
from res.config import config
import os

import logging
log = logging.getLogger(__name__)


class Excel:
    def __init__(self):
        self.filepath = config["out_folder_path"]

    def save(self, column_names, records,filename):
        try:
            df = pd.DataFrame(records, columns=column_names)
            df.to_excel(os.path.join(self.filepath,filename),index=False)
            log.info(f"{filename} saved as excel")
        except Exception as err:
            log.error(err)
            raise Exception("Failed to save file")

    def save_index_as_key_data_as_value(self,column_names,records,filename):
        try:
            df = pd.DataFrame.from_dict(records, orient="index", columns=column_names)
            df.index.name = "Employee_Number"
            df.to_excel(os.path.join(self.filepath,filename))
            log.info(f"{filename} saved as excel")
        except Exception as err:
            log.error(err.args)
            raise Exception("Failed to save file")

    def get_data_from_xlsx(self,filename):
        df = pd.read_excel(os.path.join(self.filepath,filename), index_col=None)
        log.info("read  the file.."+filename)
        return list(df.columns), df.to_records(index=False)

    def get_df_from_xlsx(self,filename):
        df = pd.read_excel(os.path.join(self.filepath, filename), index_col=None)
        return df

    def get_df_from_columns_and_tuples(self,columns,tuples):
        return pd.DataFrame(tuples,columns=columns)

    def save_df(self, df, filename):
        df.to_excel(os.path.join(self.filepath,filename),index=False)






