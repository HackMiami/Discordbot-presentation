import logging
import logging.handlers


logger = logging.getLogger(__name__)
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(funcName)s | %(message)s')

log_handler = logging.handlers.TimedRotatingFileHandler(
    filename='/var/log/bot.log',
    when='d',
    interval=1)
log_handler.setFormatter(log_formatter)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(log_formatter)

logger.addHandler(log_handler)
logger.addHandler(consoleHandler)
logger.setLevel(level=logging.INFO)
