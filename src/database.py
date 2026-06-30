import sqlite3

from src.logger import LoggerManager
from src.config import ConfigManager


class DatabaseConnector:
    """
    Handles SQLite database connections.
    """

    def __init__(self):
        self.logger = LoggerManager.get_logger()
        self.database_name = ConfigManager.get_database_name()
        self.connection = None

    @property
    def is_connected(self) -> bool:
        """
        Returns True if the database connection is active.
        """
        return self.connection is not None

    def connect(self):
        """
        Connects to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.database_name)
            self.logger.info("Database connected successfully.")

        except Exception as e:
            self.logger.error(str(e))
            raise

    def execute_query(self, query: str):
        """
        Executes a SQL query.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            self.logger.info("Query executed successfully.")

        except Exception as e:
            self.logger.error(str(e))
            raise

    def execute_script(self, file_path: str):
        """
        Executes all SQL statements from a .sql file.
        """
        try:
            with open(file_path, "r") as file:
                sql_script = file.read()

            cursor = self.connection.cursor()
            cursor.executescript(sql_script)
            self.connection.commit()

            self.logger.info(f"SQL script '{file_path}' executed successfully.")

        except Exception as e:
            self.logger.error(str(e))
            raise

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None
            self.logger.info("Database connection closed.")