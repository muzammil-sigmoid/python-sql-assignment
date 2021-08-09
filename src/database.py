from res.config import config
import psycopg2
import logging
log = logging.getLogger(__name__)


class Database:

    # configures connection uri
    def __init__(self):
        self.uri = f"dbname={config['db_name']} user={config['db_user']} password={config['db_password']}"
        self.conn = None
        self.cur = None

    # connect to database using uri and sets cursor
    def connect(self):
        try:
            self.conn = psycopg2.connect(self.uri)
            log.info("connection established")
            self.cur=self.conn.cursor()
            return self.cur
        except Exception as err:
            log.err(err)
            raise Exception("Failed to connect to Database")

    # commits the sql queries executed during execution
    # and closes the cursor and connection for the database
    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()














