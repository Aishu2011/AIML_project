class ConfigManager:
    """
    Stores application configuration settings.
    """

    LOG_FILE = "logs/application.log"
    OUTPUT_FOLDER = "outputs"
    DATABASE_NAME = "database.db"

    @classmethod
    def get_log_file(cls):
        return cls.LOG_FILE

    @classmethod
    def get_output_folder(cls):
        return cls.OUTPUT_FOLDER

    @classmethod
    def get_database_name(cls):
        return cls.DATABASE_NAME