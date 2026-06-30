import logging
import os

class LoggerManager:
    """
    Manages application logging.
    """
    
    _logger=None

    @classmethod
    def get_logger(cls):

        if cls._logger is None:
            os.makedirs("logs", exist_ok=True)

            logging.basicConfig(
                filename="logs/application.log",
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s"
            )
            cls._logger=logging.getLogger("ApplicationLogger")

        return cls._logger