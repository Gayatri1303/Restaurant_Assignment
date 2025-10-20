import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="logs//logfile.log",
    filemode="a",
    level=logging.INFO
)


class CustomLog:
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def put_info(self, message,name):
        logger.info(message,name)

    def put_warning(self, message,name):
        logger.warning( message,name)

    def put_error(self, message,name):
        logger.error( message,name)

    def put_critical(self, message,name):
        logger.critical( message,name)
