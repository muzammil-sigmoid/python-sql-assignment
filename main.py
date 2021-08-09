import logging
from src.app import App

# configuring the logger file
logging.basicConfig(filename='./logs/logs.conf', encoding='utf-8', level=logging.DEBUG)

log = logging.getLogger(__name__)

app = App()
log.info("starting app")
app.solve()
log.info("app closed ")