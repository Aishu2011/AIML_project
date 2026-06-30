from src.logger import LoggerManager


class BaseHandler:
    """
    Base class for all file handlers.
    """

    def __init__(self):
        self.logger = LoggerManager.get_logger()

    @staticmethod
    def is_supported_extension(file_path: str, extensions: tuple) -> bool:
        """
        Checks whether the file has a supported extension.
        """
        return file_path.endswith(extensions)