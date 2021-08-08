from res.config import config
import psycopg2
import logging
log = logging.getLogger(__name__)


class Database:
    def __init__(self):
        self.uri = f"dbname={config['db_name']} user={config['db_user']} password={config['db_password']}"
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.uri)
            log.info("connection established")
            self.cur=self.conn.cursor()
            return self.cur
        except Exception as err:
            log.err(err)
            raise Exception("Failed to connect to Database")

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()














