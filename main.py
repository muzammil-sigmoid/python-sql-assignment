import logging
from src.app import App

# configuring the logger file
logging.basicConfig(filename='./logs/logs.conf', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',)

log = logging.getLogger(__name__)

app = App()
log.info("starting app")
app.solve()
log.info("app closed ")